from game_engine.move import check_another_move, get_store_indexes, move_stones, prepare_move_items


def test_check_another_move():
    """Test if the player has another move"""
    pit_index = 6
    player_store_index = 6
    assert check_another_move(pit_index, player_store_index) == True

    pit_index = 7
    assert check_another_move(pit_index, player_store_index) == False


def test_get_store_indexes():
    """Test get store indexes"""
    player = 0
    player_store_index, opposite_store_index = get_store_indexes(player)
    assert player_store_index == 6
    assert opposite_store_index == 13

    player = 1
    player_store_index, opposite_store_index = get_store_indexes(player)
    assert player_store_index == 13
    assert opposite_store_index == 6


def test_prepare_move_items():
    """Test prepare move items"""
    game_state = {
        "player_turn": 0,
        "board": [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0],
        "pit_index": 0,
    }
    next_player, pit_index, stones, player_store_index, opposite_store_index = prepare_move_items(game_state)
    assert next_player == 1
    assert pit_index == 0
    assert stones == 6
    assert player_store_index == 6
    assert opposite_store_index == 13

    game_state = {
        "player_turn": 1,
        "board": [6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0],
        "pit_index": 7,
    }
    next_player, pit_index, stones, player_store_index, opposite_store_index = prepare_move_items(game_state)
    assert next_player == 0
    assert pit_index == 7
    assert stones == 7
    assert player_store_index == 13
    assert opposite_store_index == 6


def test_move_stones():
    """Test move stones"""
    game_state = {
        "player_turn": 0,
        "board": [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0],
        "pit_index": 0,
    }
    next_player, pit_index, stones, player_store_index, opposite_store_index = prepare_move_items(game_state)
    game_state = move_stones(
        game_state, stones, pit_index, player_store_index, opposite_store_index, next_player)

    print(game_state)
    assert game_state["player_turn"] == 0
    assert game_state["board"] == [0, 7, 7, 7, 7, 7, 1, 6, 6, 6, 6, 6, 6, 0]


    game_state = {
        "player_turn": 0,
        "board": [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0],
        "pit_index": 1,
    }
    next_player, pit_index, stones, player_store_index, opposite_store_index = prepare_move_items(game_state)
    game_state = move_stones(
        game_state, stones, pit_index, player_store_index, opposite_store_index, next_player)
    assert game_state["board"] == [6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0]
    assert game_state["player_turn"] == 1

    game_state = {
        "player_turn": 1,
        "board": [6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0],
        "pit_index": 7,
    }
    next_player, pit_index, stones, player_store_index, opposite_store_index = prepare_move_items(game_state)
    game_state = move_stones(
        game_state, stones, pit_index, player_store_index, opposite_store_index, next_player)
    assert game_state["board"] == [7, 0, 7, 7, 7, 7, 1, 0, 7, 7, 7, 7, 7, 1]
