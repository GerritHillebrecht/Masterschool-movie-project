from config import MAX_RATING
from storage import iStorage


def list_movies(storage: iStorage) -> None:
    """ Reads all movies from the database and lists them. """
    movies_in_storage = storage.list_movies()

    print(f'\n{len(movies_in_storage)} movies in total:')
    for idx, movie in enumerate(movies_in_storage.values()):
        print(f'{idx + 1}. {movie["title"]} ({movie["year"]}): {movie["rating"]}/{MAX_RATING}')
    print("")
