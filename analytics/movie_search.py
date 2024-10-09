from utility import get_matching_movies
from storage import iStorage


def search_movie(storage: iStorage) -> None:
    """
    Fetches all movies from the database and filters them depending on a prompted search_string.
    :return:
    """
    while True:
        matching_movies = get_matching_movies(
            input("Enter part of movie name: "),
            list(movie for movie in storage.list_movies().values())
        )

        if len(matching_movies) == 0:
            print("No movie matched your search.")
            continue

        for idx, movie in enumerate(sorted(matching_movies)):
            _, title = movie
            print(f"{idx + 1}. {title}")

        return
