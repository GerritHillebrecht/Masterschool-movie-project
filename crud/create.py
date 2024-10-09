from config import SUPPORTED_MOVIE_DATA
from storage import iStorage


def add_movie(storage: iStorage) -> None:
    """
    Loads the required Meta-data for each movie from the config file.
    Prompts the user for each meta-data-item and validates the input. Updates the database accordingly.
    :return:
    """

    movie_data = {
        prompt["name"]: validated_input(prompt)
        for prompt in SUPPORTED_MOVIE_DATA
    }
    storage.add_movie(
        title=movie_data["title"],
        year=int(movie_data["year"]),
        rating=float(movie_data["rating"]),
        poster=movie_data["poster"],
    )


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
