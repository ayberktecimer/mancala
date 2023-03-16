class NotValidGameException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message

    def __str__(self) -> str:
        return f"Game Existence Error:- {self.error_message}"
