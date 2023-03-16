# This class is used to raise an exception when a game is not valid.
class NotValidGameException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message

    def __str__(self) -> str:
        return f"Game Existence Error:- {self.error_message}"
