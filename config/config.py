from config.validators import is_float

# SELECT THE DATABASE TYPE TO USE. ENTER "JSON" OR "CSV".
SELECTED_DATABASE = "JSON"
DATABASE_FILE_NAME_CSV = "static_file_database.csv"
DATABASE_FILE_NAME_JSON = "static_file_database.json"
DATABASE_CSV_SEPERATOR_SYMBOL = ","

WELCOME_MESSAGE = """
               WELCOME TO MY
>>>>>>>>>>>>>>> IMDB RIPOFF <<<<<<<<<<<<<<<
"""

MIN_MOVIE_TITLE_LENGTH = 3
NUMBER_OF_DIGITS_IN_YEAR = 4
MIN_RATING = 0
MAX_RATING = 10

# Changes in the order of the list will break existing database data.
SUPPORTED_MOVIE_DATA = [
    {
        "name": "title",
        "label": "Title",
        "prompt": "Enter new Title: ",
        "formatter": lambda title: title.replace(DATABASE_CSV_SEPERATOR_SYMBOL, ""),
        "validator": lambda title: len(title) >= MIN_MOVIE_TITLE_LENGTH,
        "validator_message": f"Please choose a title with at least {MIN_MOVIE_TITLE_LENGTH} characters."
    },
    {
        "name": "rating",
        "label": "Rating",
        "prompt": f"Enter new Rating ({MIN_RATING}-{MAX_RATING}): ",
        "validator": lambda rating: is_float(rating) and MIN_RATING <= float(rating) <= MAX_RATING,
        "validator_message": f"Please enter a float-value between {MIN_RATING} and {MAX_RATING}."
    },
    {
        "name": "year",
        "label": "Year of release",
        "prompt": "Enter new Year of release: ",
        "validator": lambda year: year.isdigit() and len(year) == NUMBER_OF_DIGITS_IN_YEAR,
        "validator_message": f"Please a numeric value in the format <{'y' * NUMBER_OF_DIGITS_IN_YEAR}>."
    },
]
