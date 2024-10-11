from random import randrange
from storage import IStorage


def select_random_movie(storage: IStorage) -> None:
    """
    Selects a random movie from the database and prints it.
    """
    movies_in_database = storage.list_movies()
    selected_movie = list(
        movie
        for movie in movies_in_database.values()
    )[randrange(0, len(movies_in_database))]

    print(f'Your movie for tonight: {selected_movie["title"]}, it\'s rated {selected_movie["rating"]}.')
