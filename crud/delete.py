from database import read_from_database, write_to_database
from utility import index_of_matching_movie


def delete_movie() -> None:
    """
    Prompts the user for a movie name. Checks if the database has a movie that matches the prompt.
    Loops the prompt until a movie is found or the user exits. Updates the database accordingly.
    """
    while True:
        search_str = input("Enter movie name to delete ('Exit' to abort): ")
        if search_str.lower() == "exit":
            return

        movies_in_database = read_from_database()
        index = index_of_matching_movie(search_str, movies_in_database)

        if len(index) != 1:
            continue

        del movies_in_database[index[0]]
        return write_to_database(movies_in_database)
