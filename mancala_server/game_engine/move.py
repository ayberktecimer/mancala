from static.constants import NUMBER_OF_PITS, TOTAL_NUMBER_OF_HOLES, store_map


def prepare_move_items(game_state):
    '''
    This function takes a game state dictionary and prepares the necessary variables to perform a move.
    It extracts the player who will play next, the pit index from which the stones will be moved,
    the number of stones in that pit, the player's store index, and the opposite player's store index.
    :param game_state: A dictionary containing the current state of the game,
    including the board configuration, the player who has the turn, and other relevant information.
    :return:next_player: The index of the player who will play next.
            pit_index: The index of the pit from which the stones will be moved.
            stones: The number of stones in the pit.
            player_store_index: The index of the player's store.
            opposite_store_index: The index of the opposite player's store.
    '''
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
    '''
    This function takes a game state dictionary and performs a move.
    :param game_state: A dictionary containing the current state of the game,
    :param stones: The number of stones in the pit.
    :param pit_index: The index of the pit from which the stones will be moved.
    :param player_store_index: The index of the player's store.
    :param opposite_store_index: The index of the opposite player's store.
    :param next_player: The index of the player who will play next.
    :return: The updated game state dictionary.
    '''
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
    '''
    This function checks if the player gets another move.
    :param pit_index: The index of the pit from which the stones will be moved.
    :param player_store_index: The index of the player's store.
    :return: True if the player gets another move, False otherwise.
    '''
    return pit_index == player_store_index


def get_store_indexes(player):
    '''
    This function returns the indexes of the player's store and the opposite player's store.
    :param player: The index of the player.
    :return: The indexes of the player's store and the opposite player's store.
    '''
    player_store_index = store_map[player]
    opposite_store_index = store_map[1 - player]

    return player_store_index, opposite_store_index
