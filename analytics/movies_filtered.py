from database import read_from_database
from config import SUPPORTED_MOVIE_DATA, MAX_RATING


def filter_movies() -> None:
    """
    Prompts the user for filter options and prints the movie list altered by these filters.
    """
    movies = read_from_database()

    rating = prompt_and_validate_rating()
    if rating:
        movies = list(filter(lambda m: float(m["rating"]) >= rating, movies))

    start_year = prompt_and_validate_year("Enter start year (leave blank for no start year): ")
    if start_year:
        movies = list(filter(lambda m: int(m["year"]) >= start_year, movies))

    end_year = prompt_and_validate_year("Enter end year (leave blank for no end year): ")
    if end_year:
        movies = list(filter(lambda m: int(m["year"]) <= end_year, movies))

    print("Filtered Movies:")
    for movie in movies:
        print(f'{movie["title"]} ({movie["year"]}): {movie["rating"]}/{MAX_RATING}')


def prompt_and_validate_rating() -> float | None:
    """
    Prompts the user for a rating to filter and validates the input.
    :return: Returns a float for a given valid rating or None if the user wants to skip.
    """
    while True:
        rating = input("Enter minimum rating (leave blank for no minimum rating): ")
        if rating == "":
            return None

        if SUPPORTED_MOVIE_DATA[1]["validator"](rating):
            return float(rating)
        print(SUPPORTED_MOVIE_DATA[1]["validator_message"])


def prompt_and_validate_year(user_prompt: str) -> int | None:
    """
    Prompts the user for a year to filter and validates the input.
    :param user_prompt: The prompt to show to the user.
    :return: Returns an int for a given valid year or None if the user wants to skip.
    """
    while True:
        year = input(user_prompt)
        if year == "":
            return None

        if SUPPORTED_MOVIE_DATA[2]["validator"](year):
            return int(year)
        print(SUPPORTED_MOVIE_DATA[2]["validator_message"])
