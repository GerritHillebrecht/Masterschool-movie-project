from os import path
from config.config import DATABASE_FILE_NAME_CSV, STORAGE_CSV_SEPERATOR_SYMBOL, SUPPORTED_MOVIE_DATA


def read_database_csv() -> list[dict]:
    """
    Reads all movies from the file-database and converts them in a list of dictionaries, each representing a movie.
    :return: A list of movies from the database as dictionaries.
    """
    if not path.exists(DATABASE_FILE_NAME_CSV):
        print("Couldn't find database-file. Creating a new file.")
        open(DATABASE_FILE_NAME_CSV, "x")
        return []

    with open(DATABASE_FILE_NAME_CSV, "r") as handle:
        return convert_from_database(handle.readlines())


def write_database_csv(movies: list[dict]) -> None:
    """
    Takes in a list of movies and converts them to a string. Saves this string into the database file.
    :param movies: List of all movies to be saved into the file.
    :return: No return values.
    """
    with open(DATABASE_FILE_NAME_CSV, "w") as handle:
        handle.write(convert_to_database(movies))


def convert_from_database(lines) -> list[dict]:
    """
    Converts the data from the database into usable data as a list of dictionaries.
    :param lines: All lines read from the database-file.
    :return: Returns a list of dictionaries representing the movies.
    """
    return [
        {
            # Reads the data structure from the config-file
            SUPPORTED_MOVIE_DATA[idx]["name"]: value
            # Strips all trailing " " and "\n". Splits by the database seperator-symbol from the config-file.
            for idx, value in enumerate(line.strip().split(STORAGE_CSV_SEPERATOR_SYMBOL))
        }
        for line in lines
    ]


def convert_to_database(movies: list[dict]) -> str:
    """
    Converts the list of dictionaries format for movies to work with back into lines for the .csv database.
    :param movies: The movies to be converted.
    :return: Returns writeable data for the database.
    """
    return "".join(
        [
            STORAGE_CSV_SEPERATOR_SYMBOL.join([str(val) for val in movie.values()]) + "\n"
            for movie in movies
        ]
    )
