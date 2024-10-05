from database import read_from_database
from config import MAX_RATING


def list_movies() -> None:
    """
    Reads all movies from the database and lists them.
    :return:
    """
    movies = read_from_database()

    print(f'\n{len(movies)} movies in total:')
    for idx, movie in enumerate(movies):
        print(f'{idx + 1}. {movie["title"]} ({movie["year"]}): {movie["rating"]}/{MAX_RATING}')
    print("")
