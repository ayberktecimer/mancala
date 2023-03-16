from static.constants import store_map


def calculate_score(game_state):
    '''
    Calculate the score for each player
    :param game_state: the current game state
    :return: the score for each player
    '''
    player_1_score = game_state["board"][store_map[0]] + sum(
        game_state["board"][0 : store_map[0]]
    )
    player_2_score = game_state["board"][store_map[1]] + sum(
        game_state["board"][store_map[0] + 1 : store_map[1]]
    )

    return player_1_score, player_2_score
