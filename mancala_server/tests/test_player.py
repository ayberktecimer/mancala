from game_engine.player import calculate_score


def test_player_score():
    game_state = {
        "player_turn": 0,
        "board": [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0],
        "pit_index": 0,
    }
    player_1_score, player_2_score = calculate_score(game_state)
    assert player_1_score == 36
    assert player_2_score == 36

    game_state = {
        "player_turn": 0,
        "board": [6, 0, 6, 7, 7, 7, 1, 7, 7, 6, 6, 6, 6, 0],
        "pit_index": 7,
    }
    player_1_score, player_2_score = calculate_score(game_state)
    assert player_1_score == 34
    assert player_2_score == 38