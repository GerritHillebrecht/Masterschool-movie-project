from database import read_from_database
from statistics import mean
from math import ceil


def stats() -> None:
    """
    Prints various stats about the movies in the database.
    :return:
    """
    movies_in_database = read_from_database()

    # average rating
    avg = mean([
        # Input is type-validated, no validation needed here.
        float(movie["rating"])
        for movie in movies_in_database
    ])
    print("\nAverage rating:", format(avg, ".1f"))

    # median rating
    median = float(movies_in_database[len(movies_in_database) // 2]["rating"])

    if len(movies_in_database) % 2 != 0 and len(movies_in_database) > 1:
        median = (median + float(movies_in_database[ceil(len(movies_in_database) / 2)]["rating"])) / 2

    print("Median rating:", format(median, ".1f"))

    # best movie(s)
    # sort by rating
    ranked_by_rating = sorted(movies_in_database, key=lambda movie: float(movie["rating"]), reverse=True)

    # filter by highest ranking and sort alphabetically.
    highest_ratings = sorted(filter(
        lambda movie: movie["rating"] == ranked_by_rating[0]["rating"],
        ranked_by_rating
    ), key=lambda movie: movie["title"])

    # Print depending on the list length
    if len(highest_ratings) > 1:
        print("The movies with the highest ratings are: ")
    for movie in highest_ratings:
        if len(highest_ratings) > 1:
            print("-> ", end="")
        print(f'Best movie: {movie["title"]}, {movie["rating"]}')

    # worst movies(s)
    # sort by rating
    ranked_by_rating = sorted(movies_in_database, key=lambda movie: float(movie["rating"]))

    # filter by lowest ranking and sort alphabetically.
    lowest_rankings = sorted(filter(
        lambda movie: movie["rating"] == ranked_by_rating[0]["rating"],
        ranked_by_rating
    ), key=lambda movie: movie["title"])

    # Print depending on the list length
    if len(lowest_rankings) > 1:
        print("The movies with the lowest ratings are: ")
    for movie in lowest_rankings:
        if len(lowest_rankings) > 1:
            print("-> ", end="")
        print(f'Worst movie: {movie["title"]}, {movie["rating"]}')
