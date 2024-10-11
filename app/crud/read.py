from config import MAX_RATING
from storage import IStorage


def list_movies(storage: IStorage) -> None:
    """ Reads all movies from the database and lists them. """
    movies_in_storage = storage.list_movies()

    print(f'\n{len(movies_in_storage)} movies in total:')
    for idx, movie in enumerate(movies_in_storage.values()):
        i = idx + 1
        title = movie["title"]
        year = movie["year"]
        rating = f"{movie["rating"]}/{MAX_RATING}"
        notes = f"Notes: {movie["notes"]}" if movie.get("notes") else ""

        print(f'{i}. {title} ({year}): {rating}. {notes}')
    print("")
