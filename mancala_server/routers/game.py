import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse

from exceptions.exceptions import NotValidGameException
from game_engine.game import initialize_game, make_move
from models.rest_models.models import Move, MoveResponse

logger = logging.getLogger(__name__)
router = APIRouter(
    tags=["game"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def home():
    response = RedirectResponse(url='/docs')
    return response


@router.get("/initialize_game")
def _initialize_game():

    try:
        return initialize_game()

    except Exception as e:
        logger.error(e)
        return JSONResponse(content={"message": type(e).__name__}, status_code=500)


@router.post("/make_move", response_model=MoveResponse)
def _make_move(move_item: Move) -> JSONResponse:
    try:
        move_response = make_move(move_item)
        return JSONResponse(content=move_response.dict(), status_code=200)

    except NotValidGameException as e:
        logger.error(e)
        return JSONResponse(
            content={"message": type(e).__name__, "error_message": e.error_message},
            status_code=400,
        )

    except Exception as e:
        logger.error(e)
        return JSONResponse(content={"message": type(e).__name__}, status_code=500)
