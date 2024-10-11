from data_access import omdb
from storage import IStorage


def add_movie(storage: IStorage) -> None:
    """
    Loads the required Meta-data for each movie from the config file.
    Prompts the user for each meta-data-item and validates the input. Updates the database accordingly.
    """
    movie_title = prompt_title()

    if not movie_title:
        return

    try:
        movie_data = omdb.fetch_movie(movie_title)
    except ValueError:
        print(f"Couldn't find movie {movie_title}")
        return

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
    """
    Prompts the user to enter a movie title.

    This function repeatedly asks the user to input a movie title until a non-empty
    title is provided or the user chooses to abort by entering an empty string.

    Returns:
        str or None: The movie title entered by the user, or None if the user aborts.

    Note:
        - If the user enters an empty string, the function prints a message and returns None.
        - The function trims leading and trailing whitespace from the user's input.
    """
    while True:
        title = input("Which movie do you want to add (Empty to abort)? ")

        # Guard clause: Exit
        if not title:
            print("No movie was added to the storage.")
            return

        return title.strip()


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
