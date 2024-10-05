from os import path
import json
from config import DATABASE_FILE_NAME_JSON


def read_database_json() -> list:
    if not path.exists(DATABASE_FILE_NAME_JSON):
        open(DATABASE_FILE_NAME_JSON, "x")
        return []

    with open(DATABASE_FILE_NAME_JSON, "r") as handle:
        database_data = handle.read()
        return json.loads(database_data) if len(database_data) > 0 else []


def write_database_json(movies: list[dict]) -> None:
    if not path.exists(DATABASE_FILE_NAME_JSON):
        open(DATABASE_FILE_NAME_JSON, "x")

    with open(DATABASE_FILE_NAME_JSON, "w") as handle:
        handle.write(json.dumps(movies))
