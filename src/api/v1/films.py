import uuid
from http import HTTPStatus
from typing import List
from typing import Union

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from pydantic import BaseModel
from services.film import FilmService
from services.film import get_film_service

router = APIRouter()

FILM_ERROR_NO_ITEM_FOR_REQUEST = 'No films found based on your request'
FILM_ERROR_ITEM_NOT_FOUND = 'The film is not found'
FILM_ERROR_NO_SIMILAR_FILM = 'No similar films found'
FILM_ERROR_WRONG_SORT_PARAMETER = 'Wrong sort parameter'

class UUIDModel(BaseModel):
    uuid: uuid.UUID

class Film(UUIDModel):
    title: str
    imdb_rating: Union[float, None]

class FilmOut(BaseModel):
    uuid: uuid.UUID
    title: str
    imdb_rating: Union[float, None]


@router.get('/search', summary='Search filmwork with words in detailed information')
async def film_search(
    q: str = Query(None, alias='query'),
    page: int = Query(1, alias='page[number]'),
    size: int = Query(50, alias='page[size]'),
    film_service: FilmService = Depends(get_film_service),
) -> List[FilmOut]:
    """
    Return a list of filmworks with words in detailed information.

    Query parameters:
    - **query** - search phrase or word.

    Parameters of pagination:
    - **page[size]**: the number of elements per page.
    - **page[number]**: the number of the current page.
    """
    films = await film_service.search_objects(q, 'Film', page, size)
    if not films:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=FILM_ERROR_NO_ITEM_FOR_REQUEST)
    return [FilmOut(uuid=film.uuid, title=film.title, imdb_rating=film.imdb_rating) for film in films]

