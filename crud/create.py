from config import SUPPORTED_MOVIE_DATA
from storage import IStorage
from data_access import omdb


def add_movie(storage: IStorage) -> None:
    """
    Loads the required Meta-data for each movie from the config file.
    Prompts the user for each meta-data-item and validates the input. Updates the database accordingly.
    """
    movie_title = prompt_title()
    try:
        movie_data = omdb.fetch_movie(movie_title)
    except ValueError:
        print(f"Couldn't find movie {movie_title}")
        return

    # old version
    # movie_data = {
    #     prompt["name"]: validated_input(prompt)
    #     for prompt in SUPPORTED_MOVIE_DATA
    # }

    try:
        storage.add_movie(
            title=movie_data["Title"],
            year=int(movie_data["Year"]),
            rating=float(movie_data["imdbRating"]),
            poster=movie_data["Poster"],
        )
    except ValueError:
        print(f"The movie {movie_title} is already in the storage.")


def prompt_title():
    while True:
        title = input("Which movie do you want to add? ")

        if not title:
            print("Please provide a title.")
            continue

        return title


def validated_input(prompt: dict) -> str:
    """
    Prompts the user for the passed meta-data-item until the validation function accepts the input.
    Also formats the input according to the config file. E.g. the title string cannot have symbols that are used
    within in the .csv of the database. These are replaced.
    :param prompt: The meta-data prompt item from the config file.
    """
    while True:
        selected_prompt = input(prompt["prompt"])

        if prompt["validator"](selected_prompt):
            return prompt["formatter"](selected_prompt) if "formatter" in prompt else selected_prompt

        print(prompt["validator_message"])
