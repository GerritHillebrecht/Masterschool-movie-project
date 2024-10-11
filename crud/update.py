from config import SUPPORTED_MOVIE_DATA
from storage import IStorage


def update_movie(storage: IStorage) -> None:
    """
    Prompts the user for the movie title to update. If found, prompts for an updated rating.
    Updates the database accordingly.
    :return:
    """
    while True:
        movie_title = input("Enter movie name ('Exit' to abort): ")

        if not movie_title:
            print("Please enter a movie name.")
            continue

        # Guard clause: Exit
        if movie_title.lower() == "exit":
            return

        new_rating = prompt_updated_rating()

        storage.update_movie(
            movie_title,
            new_rating
        )

        print(f"{movie_title}'s rating updated to {new_rating}")


def prompt_updated_rating() -> float:
    """
    Prompts the user for an updated rating value and validates it according to the config file.
    :return: Returns the updated rating as a float.
    """
    while True:
        user_input = input("Enter new movie rating: ")
        if SUPPORTED_MOVIE_DATA[1]["validator"](user_input):
            return float(user_input)
        print(SUPPORTED_MOVIE_DATA[1]["validator_message"])
