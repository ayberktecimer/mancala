"""
The Player class is a basic class that represents a player in a game. It has attributes such as name, score, and ID.
The Player class is inherited by the HumanPlayer and AIPlayer classes which use the Factory Design Pattern to create
instances of the Player class.

The PlayerFactory class is responsible for creating the appropriate type of player based on the player_type
parameter that is passed to it. It creates instances of the HumanPlayer and AIPlayer classes using the create_player()
method, which takes in the player_type, name, and ID of the player.

The HumanPlayer and AIPlayer classes are subclasses of the Player class, and their constructors simply call the
superclass constructor using super().init() method.

The Factory Design Pattern used in this class provides a simple way to create objects without exposing the creation
logic to the client. This allows for more flexibility in creating objects, and makes it easy to add new
types of players in the future.
"""
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
