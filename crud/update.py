from utility import index_of_matching_movie
from database import read_from_database, write_to_database
from config import SUPPORTED_MOVIE_DATA


def update_movie() -> None:
    """
    Prompts the user for the movie title to update. If found, prompts for an updated rating.
    Updates the database accordingly.
    :return:
    """
    while True:
        search_str = input("Enter movie name (Exit to abort): ")

        # Guard clause: Exit
        if search_str.lower() == "exit":
            return

        movies_in_database = read_from_database()
        index: list[int] = index_of_matching_movie(search_str, movies_in_database)

        if len(index) != 1:
            continue

        movies_in_database[index[0]]["rating"] = prompt_updated_rating()
        write_to_database(movies_in_database)
        return


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
