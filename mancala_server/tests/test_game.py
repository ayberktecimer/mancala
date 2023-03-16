from models.entity_models.board import Board
from models.entity_models.game import Game
from models.entity_models.player import PlayerFactory
from game_engine.game import get_winner, check_game_over, check_all_holes_empty


def test_get_winner_player1_wins():
    """Test that player 1 is declared the winner."""
    board = Board()
    factory = PlayerFactory()
    player_1 = factory.create_player("human", "Player 1", 0)
    player_2 = factory.create_player("human", "Player 2", 1)
    game = Game(board, [player_1, player_2])

    # set up the board with a higher score for player 1
    game.board.board_list = [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1]

    game_state = {
        "game_id": '0',
        "board": game.board.board_list,
        "player_1": game.players[0].name,
        "player_2": game.players[1].name,
        "player_1_score": game.players[0].score,
        "player_2_score": game.players[1].score,
        "player_turn": 0,
        "game_over": True,
        "winner": "",
    }
    # call the method being tested
    result = get_winner(game_state)
    # assert that player 1 is declared the winner
    assert result == "Player 1"


def test_get_winner_player2_wins():
    """Test that player 2 is declared the winner."""
    board = Board()
    factory = PlayerFactory()
    player_1 = factory.create_player("human", "Player 1", 0)
    player_2 = factory.create_player("human", "Player 2", 1)
    game = Game(board, [player_1, player_2])

    # set up the board with a higher score for player 1
    game.board.board_list = [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3]

    game_state = {
        "game_id": '0',
        "board": game.board.board_list,
        "player_1": game.players[0].name,
        "player_2": game.players[1].name,
        "player_1_score": game.players[0].score,
        "player_2_score": game.players[1].score,
        "player_turn": 0,
        "game_over": True,
        "winner": "",
    }
    # call the method being tested
    result = get_winner(game_state)
    # assert that player 1 is declared the winner
    assert result == "Player 2"


def test_get_winner_tie():
    """Test that a tie is declared."""
    board = Board()
    factory = PlayerFactory()
    player_1 = factory.create_player("human", "Player 1", 0)
    player_2 = factory.create_player("human", "Player 2", 1)
    game = Game(board, [player_1, player_2])

    # set up the board with a higher score for player 1
    game.board.board_list = [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2]

    game_state = {
        "game_id": '0',
        "board": game.board.board_list,
        "player_1": game.players[0].name,
        "player_2": game.players[1].name,
        "player_1_score": game.players[0].score,
        "player_2_score": game.players[1].score,
        "player_turn": 0,
        "game_over": True,
        "winner": "",
    }
    # call the method being tested
    result = get_winner(game_state)
    # assert that player 1 is declared the winner
    assert result == "Tie"


