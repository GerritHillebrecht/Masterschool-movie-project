from random import randrange
from database import read_from_database


def select_random_movie() -> None:
    """
    Selects a random movie from the database and prints it.
    """
    movies_in_database = read_from_database()
    selected_movie = movies_in_database[randrange(0, len(movies_in_database))]

    print(f'Your movie for tonight: {selected_movie["title"]}, it\'s rated {selected_movie["rating"]}.')
