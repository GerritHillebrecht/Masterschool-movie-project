from config import SELECTED_DATABASE
from database.storage_csv_methods import write_database_csv, read_database_csv
from database.storage_json_methods import write_database_json, read_database_json


def write_to_database(
        movies: list[dict],
        selected_database=SELECTED_DATABASE
) -> None:
    match selected_database:
        case "JSON":
            write_database_json(movies)
        case "CSV":
            write_database_csv(movies)
        case _:
            write_database_json(movies)


def read_from_database() -> list[dict]:
    return read_database_json() if SELECTED_DATABASE == "JSON" else read_database_csv()
