from collections import OrderedDict
import crud
import analytics
from web_gen import generate_website

dispatcher: OrderedDict[str, dict] = OrderedDict({
    # 1. Read
    "movies_list": {
        "name": "List movies",
        "function": lambda storage: crud.list_movies(storage)
    },

    # 2. Create
    "movie_add": {
        "name": "Add movie",
        "function": lambda storage: crud.add_movie(storage)
    },

    # 3. Delete
    "movie_delete": {
        "name": "Delete movie",
        "function": lambda storage: crud.delete_movie(storage)
    },

    # 4. Update
    "movie_update": {
        "name": "Update movie",
        "function": lambda storage: crud.update_movie(storage)
    },

    # 5. Read and mutate
    "stats": {
        "name": "Stats",
        "function": lambda storage: analytics.stats(storage)
    },

    # 6. Random
    "random": {
        "name": "Random movie",
        "function": lambda storage: analytics.select_random_movie(storage)
    },

    # 7. Search
    "search_movie": {
        "name": "Search movie",
        "function": lambda storage: analytics.search_movie(storage)
    },

    # 8. Movies sorted by rating
    "print_movies_by_rating": {
        "name": "Movies sorted by rating",
        "function": lambda storage: analytics.print_movies_by_rating(storage)
    },

    # 9. Movies sorted by year
    "print_movies_by_release": {
        "name": "Movies sorted by year",
        "function": lambda storage: analytics.print_movies_by_release(storage)
    },

    # 10. Filter movies
    "filter_movies": {
        "name": "Filter movies",
        "function": lambda storage: analytics.filter_movies(storage)
    },

    # 11. Generate Website
    "generate_website": {
        "name": "Generate Website",
        "function": lambda storage: generate_website(storage)
    }
})
