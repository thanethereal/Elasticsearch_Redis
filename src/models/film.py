from typing import List

import orjson
import uuid as uuid
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class UUIDModel(BaseModel):
    uuid: str



class Film(UUIDModel):
    title: str
    imdb_rating: float | None
    description: str | None

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
