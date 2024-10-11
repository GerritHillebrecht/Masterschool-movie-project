from storage import IStorage
from utility import create_movie_key


def update_movie(storage: IStorage) -> None:
    """
    Prompts the user for the movie title to update. If found, prompts for an updated rating.
    Updates the database accordingly.
    """
    movies = storage.list_movies()

    while True:
        movie_title = input("Enter movie name ('Exit' to abort): ")

        if not movie_title:
            print(f"Please enter a movie name.")
            continue

        # Guard clause: Exit
        if movie_title.lower() == "exit":
            return

        if create_movie_key(movie_title) not in movies:
            print(f"Movie {movie_title} could not be found in the storage.")
            continue

        notes = prompt_movie_notes()

        storage.update_movie(
            movie_title,
            notes
        )

        return print(f"{movie_title}'s notes updated to: {notes}")


def prompt_movie_notes() -> str:
    """
    Prompts the user for an updated rating value and validates it according to the config file.
    :return: Returns the updated rating as a float.
    """
    while True:
        movie_notes = input("Enter movie notes: ")

        if not movie_notes:
            print("Please provide some notes. You cannot skip this, because fuck you that's why.")
            continue

        return movie_notes
