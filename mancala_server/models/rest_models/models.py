from pydantic import BaseModel


class Move(BaseModel):
    game_id: int
    pit_index: int


class MoveResponse(BaseModel):
    game_id: int
    board: list
    player_1: str
    player_2: str
    player_1_score: int
    player_2_score: int
    player_turn: int
    game_over: bool
    winner: str
