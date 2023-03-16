class Player:
    def __init__(self, name, id):
        self.name = name
        self.score = 0
        self.id = id
        self.store_index = (id + 1) * 6 + id


class PlayerFactory:
    def create_player(self, player_type, name, id):
        if player_type == "human":
            return HumanPlayer(name, id)
        elif player_type == "ai":
            return AIPlayer(name, id)
        else:
            raise ValueError("Invalid player type.")


class HumanPlayer(Player):
    def __init__(self, name, id):
        super().__init__(name, id)


class AIPlayer(Player):
    def __init__(self, name, id):
        super().__init__(name, id)
