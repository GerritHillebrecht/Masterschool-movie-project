from config import SUPPORTED_MOVIE_DATA
from storage import IStorage


def update_movie(storage: IStorage) -> None:
    """
    Prompts the user for the movie title to update. If found, prompts for an updated rating.
    Updates the database accordingly.
    """
    while True:
        movie_title = input("Enter movie name ('Exit' to abort): ")

        if not movie_title:
            print(f"Could not find movie {movie_title}. Please enter a movie name.")
            continue

        # Guard clause: Exit
        if movie_title.lower() == "exit":
            return

        notes = prompt_movie_notes()

        storage.update_movie(
            movie_title,
            notes
        )

        print(f"{movie_title}'s rating updated to {notes}")


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
