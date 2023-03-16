from exceptions.exceptions import NotValidGameException
from game_engine.move import move_stones, prepare_move_items
from game_engine.player import calculate_score
from models.entity_models.board import Board
from models.entity_models.game import Game
from models.entity_models.player import PlayerFactory
from models.rest_models.models import MoveResponse
from static.constants import store_map

games = {}


def initialize_game():
    # This function initializes a game by creating two human players, a board, and a game object.
    # The function returns the game state as a JSON object.
    global games
    factory = PlayerFactory()
    player_1 = factory.create_player("human", "Marco", 0)
    player_2 = factory.create_player("human", "Thomas", 1)
    board = Board()
    game = Game(board, [player_1, player_2])
    game_state = {
        "game_id": len(games),
        "board": game.board.board_list,
        "player_1": game.players[0].name,
        "player_2": game.players[1].name,
        "player_1_score": game.players[0].score,
        "player_2_score": game.players[1].score,
        "player_turn": 0,
        "game_over": False,
        "winner": "",
    }

    games[game_state["game_id"]] = game_state
    return game_state


def make_move(move_info):
    '''
    This function makes a move in the game by updating the game state based on the move information provided.
    The function prepares the items needed to make the move, moves the stones, calculates the score, and checks if the game is over.
    The function returns a MoveResponse object that contains the updated game state.
    :param move_info:
    :return: MoveResponse
    '''
    game_state = games.get(move_info.game_id)
    if not game_state:
        raise NotValidGameException(
            "Game with id {} does not exist".format(move_info.game_id)
        )
    # game_state = games[move_info['game_id']]
    game_state["pit_index"] = move_info.pit_index

    (
        next_player,
        pit_index,
        stones,
        player_store_index,
        opposite_store_index,
    ) = prepare_move_items(game_state)

    game_state = move_stones(
        game_state,
        stones,
        pit_index,
        player_store_index,
        opposite_store_index,
        next_player,
    )

    game_state["player_1_score"], game_state["player_2_score"] = calculate_score(
        game_state
    )
    # check if game is over
    game_state["game_over"], game_state["winner"] = check_game_over(game_state)

    # return response using MoveResponse
    return MoveResponse(**game_state)


def check_game_over(game_state):
    '''
    This function checks if the game is over by checking if all holes are empty.
    If all holes are empty, the function sets the game over flag to True and determines the winner.
    The function returns a tuple containing the game over flag and the winner.
    :param game_state:
    :return: tuple
    '''
    if check_all_holes_empty(game_state["game_id"]) != 0:
        game_state["game_over"] = True
        game_state["winner"] = get_winner(game_state)

    return game_state["game_over"], game_state["winner"]


def check_all_holes_empty(game_id):
    '''
    This function checks if all holes are empty for a given game ID.
    If all holes are empty on one player's side, the function returns the corresponding player (1 or 2).
    If all holes are empty on both sides, the function returns 0.
    :param game_id:
    :return: int
    '''
    game_state = games[game_id]
    for i in range(0, store_map[0]):
        if game_state["board"][i] != 0:
            break
        if i == store_map[0] - 1:
            return 1

    for i in range(store_map[0] + 1, store_map[1]):
        if game_state["board"][i] != 0:
            break
        if i == store_map[1] - 1:
            return 2

    return 0


def get_winner(game_state):
    '''
    This function determines the winner of the game by calculating the scores of both players and comparing them.
    If player 1 has a higher score, the function returns player 1's name.
    If player 2 has a higher score, the function returns player 2's name.
    If the scores are tied, the function returns "Tie".
    :param game_state: dict
    :return: str
    '''
    player_1_score, player_2_score = calculate_score(game_state)
    if player_1_score > player_2_score:
        return game_state["player_1"]
    elif player_2_score > player_1_score:
        return game_state["player_2"]
    else:
        return "Tie"
