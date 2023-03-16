from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os


router = APIRouter(
    tags=["rules"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_rules")
def get_rules():
    """Get the rules of the game."""
    os.chdir(".")  # Go up one directory from working directory
    static_dir = os.path.join(os.getcwd(), "static")
    file_path = os.path.join(static_dir, 'game_rules.txt')
    # read each line of the file and append it to a list
    with open(file_path) as f:
        rules = f.readlines()
    return JSONResponse(content={"message": rules}, status_code=200)