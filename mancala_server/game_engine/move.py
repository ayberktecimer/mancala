from static.constants import NUMBER_OF_PITS, TOTAL_NUMBER_OF_HOLES, store_map


def prepare_move_items(game_state):
    next_player = 1 - game_state["player_turn"]

    pit_index = game_state["pit_index"]
    stones = game_state["board"][game_state["pit_index"]]

    player_store_index, opposite_store_index = get_store_indexes(
        game_state["player_turn"]
    )

    return next_player, pit_index, stones, player_store_index, opposite_store_index


def move_stones(
    game_state, stones, pit_index, player_store_index, opposite_store_index, next_player
):
    game_state["board"][pit_index] = 0
    while stones > 0:
        pit_index = (pit_index + 1) % TOTAL_NUMBER_OF_HOLES

        if pit_index == opposite_store_index:
            continue

        if stones == 1:
            if check_another_move(pit_index, player_store_index):
                game_state["board"][pit_index] += 1
                next_player = game_state["player_turn"]
                break
            if player_store_index > pit_index >= player_store_index - 6:
                opposite_index = NUMBER_OF_PITS - pit_index

                if (
                    game_state["board"][pit_index] == 0
                    and game_state["board"][opposite_index] > 0
                ):
                    game_state["board"][player_store_index] += (
                        game_state["board"][opposite_index] + 1
                    )
                    game_state["board"][opposite_index] = 0
                    break

        game_state["board"][pit_index] += 1
        stones -= 1
    game_state["player_turn"] = next_player
    return game_state


def check_another_move(pit_index, player_store_index):
    # If the last stone is placed in the player's store, the player gets another turn.
    return pit_index == player_store_index


def get_store_indexes(player):
    player_store_index = store_map[player]
    opposite_store_index = store_map[1 - player]

    return player_store_index, opposite_store_index
