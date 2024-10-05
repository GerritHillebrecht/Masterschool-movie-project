def index_of_matching_movie(search_str: str, movies: list[dict]) -> list[int]:
    """
    Takes in a search string and a list of dictionaries.
    Returns a list of int representing the occurrences of the search_str in the provided movie-list as indices.
    :param search_str: The substr to search for.
    :param movies: The movies to be searched.
    :return: A list of matching indices. Best case scenario: Only one item in the list.
    """
    matching_movies = get_matching_movies(search_str, movies)

    if len(matching_movies) == 0:
        print(f"Movie {search_str} doesn't exist!")
        return []

    if len(matching_movies) > 1:
        print(f"Possible matches (choose more specifically):")
        for movie in matching_movies:
            idx, movie = movie
            print(f"{idx + 1}. {movie}")

    return [
        idx
        for idx, movie_title in matching_movies
    ]


def get_matching_movies(search_str, movies) -> list[tuple[int, str]]:
    """
    Matches all movies of the database against the search_str and returns the movie titles and indices.
    :param search_str: The search substr.
    :param movies: The movie-list from the database.
    :return: Filtered list of matching movies including indices.
    """
    # Using a set in case two movies have the exact same name.
    # Should make the user choose the movie to delete or update by index instead for matching cases,
    # but it's not part of the assignment, so all movies with exactly matching names will get deleted.
    return list(set([
        (idx, movie["title"])
        for idx, movie in enumerate(movies)
        if search_str.lower() in movie["title"].lower()
    ]))
