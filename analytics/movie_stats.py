from storage import iStorage
from statistics import mean
from math import ceil


def stats(storage: iStorage) -> None:
    """
    Prints various stats about the movies in the database.
    """
    movies_in_storage = storage.list_movies()
    num_movies_in_storage = len(movies_in_storage)

    movies_sorted = list(sorted(
        (movie for movie in movies_in_storage.values()),
        key=lambda movie: float(movie["rating"]),
        reverse=True
    ))

    # average rating
    avg = mean(float(movie["rating"]) for movie in movies_sorted)
    print("\nAverage rating:", format(avg, ".1f"))

    # median rating
    median = movies_sorted[num_movies_in_storage // 2]["rating"]

    if num_movies_in_storage % 2 != 0 and num_movies_in_storage > 1:
        median = (median + movies_sorted[ceil(num_movies_in_storage / 2)]["rating"]) / 2

    print("Median rating:", format(median, ".1f"))

    # best movie(s)
    # filter by highest ranking and sort alphabetically.
    highest_ratings = sorted(filter(
        lambda movie: movie["rating"] == movies_sorted[0]["rating"],
        movies_sorted
    ), key=lambda movie: movie["title"])

    # Print depending on the list length
    print_ranked_movies(highest_ratings)

    # worst movies(s)
    # sort by rating
    movies_sorted_reverse = movies_sorted[::-1]

    # filter by lowest ranking and sort alphabetically.
    lowest_rankings = sorted(filter(
        lambda movie: movie["rating"] == movies_sorted_reverse[0]["rating"],
        movies_sorted_reverse
    ), key=lambda movie: movie["title"])

    # Print depending on the list length
    print_ranked_movies(lowest_rankings, ("lowest", "Worst"))


def print_ranked_movies(movies, rank_type=("highest", "Best")):
    # Print depending on the list length
    if len(movies) > 1:
        print(f"The movies with the {rank_type[0]} ratings are: ")
    for movie in movies:
        if len(movies) > 1:
            print("-> ", end="")
        print(f'{rank_type[1]} movie: {movie["title"]}, {movie["rating"]}')
