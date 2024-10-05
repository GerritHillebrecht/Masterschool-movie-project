from utility import get_matching_movies
from database import read_from_database


def search_movie() -> None:
    """
    Fetches all movies from the database and filters them depending on a prompted search_string.
    :return:
    """
    while True:
        matching_movies = get_matching_movies(
            input("Enter part of movie name: "),
            read_from_database()
        )

        if len(matching_movies) == 0:
            continue

        for idx, movie in enumerate(sorted(matching_movies)):
            _, title = movie
            print(f"{idx + 1}. {title}")

        return
