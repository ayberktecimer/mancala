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
    """This method starts the game."""
    # return game attributes as json
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
    if check_all_holes_empty(game_state["game_id"]) != 0:
        game_state["game_over"] = True
        game_state["winner"] = get_winner(game_state)

    return game_state["game_over"], game_state["winner"]


def check_all_holes_empty(game_id):
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
    player_1_score, player_2_score = calculate_score(game_state)
    if player_1_score > player_2_score:
        return game_state["player_1"]
    elif player_2_score > player_1_score:
        return game_state["player_2"]
    else:
        return "Tie"
