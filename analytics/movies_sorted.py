from storage import iStorage


def print_movies_by_rating(storage: iStorage) -> None:
    """
    Prints all movies ordered by rating.
    """
    movies_in_database = storage.list_movies()
    print("")
    for idx, movie in enumerate(sorted(
            movies_in_database.values(),
            key=lambda m: float(m["rating"]),
            reverse=True)
    ):
        print(f'{idx + 1}. {movie["title"]} ({movie["year"]}): {movie["rating"]}')
    print("")


def print_movies_by_release(storage: iStorage) -> None:
    """
    Prints all movies ordered by release.
    """
    movies_in_database = storage.list_movies()
    asc: bool = prompt_order_of_release()

    print("")
    for idx, movie in enumerate(sorted(
            movies_in_database.values(),
            key=lambda m: m["year"],
            reverse=asc
    )):
        print(f'{idx + 1}. {movie["title"]} ({movie["year"]}): {movie["rating"]}')
    print("")


def prompt_order_of_release() -> bool:
    """
    Prompts the user for asc or desc order of release.
    :return: Boolean, where True means DESC.
    """
    while True:
        order_selection = input("Do you want the latest movies first? (Y/N)").lower()
        if order_selection not in ["y", "n"]:
            print("Yes or no? Not that hard.")
            continue

        return order_selection == "y"
