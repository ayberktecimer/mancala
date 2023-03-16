from pydantic import BaseModel

# Pydantic models for a game move and its response


class Move(BaseModel): # Represents a move in a game
    game_id: int
    pit_index: int


class MoveResponse(BaseModel): # Represents the response after a move is made
    game_id: int
    board: list
    player_1: str
    player_2: str
    player_1_score: int
    player_2_score: int
    player_turn: int
    game_over: bool
    winner: str
