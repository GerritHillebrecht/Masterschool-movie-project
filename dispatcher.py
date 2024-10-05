from collections import OrderedDict
import crud
import analytics

dispatcher: OrderedDict[str, dict] = OrderedDict({
    # 1. Read
    "movies_list": {
        "name": "List movies",
        "function": crud.list_movies
    },

    # 2. Create
    "movie_add": {
        "name": "Add movie",
        "function": crud.add_movie
    },

    # 3. Delete
    "movie_delete": {
        "name": "Delete movie",
        "function": crud.delete_movie
    },

    # 4. Update
    "movie_update": {
        "name": "Update movie",
        "function": crud.update_movie,
    },

    # 5. Read and mutate
    "stats": {
        "name": "Stats",
        "function": analytics.stats
    },

    # 6. Random
    "random": {
        "name": "Random movie",
        "function": analytics.select_random_movie
    },

    # 7. Search
    "search_movie": {
        "name": "Search movie",
        "function": analytics.search_movie
    },

    # 8. Movies sorted by rating
    "print_movies_by_rating": {
        "name": "Movies sorted by rating",
        "function": analytics.print_movies_by_rating
    },

    # 9. Movies sorted by year
    "print_movies_by_release": {
        "name": "Movies sorted by year",
        "function": analytics.print_movies_by_release
    },

    # 10. Filter movies
    "filter_movies": {
        "name": "Filter movies",
        "function": analytics.filter_movies
    }
})
