"""
OMDB API Interaction Module

This module provides functions to interact with the Open Movie Database (OMDB) API.
It allows fetching movie information and poster images based on movie titles.

Functions:
    fetch_movie(title: str) -> dict: Fetches detailed movie information from the OMDB API.
    fetch_poster(title: str) -> dict: Fetches poster image information for a movie from the OMDB API.

Dependencies:
    - requests: For making HTTP requests to the OMDB API.
    - time: For implementing retry delays.
    - os: For accessing environment variables.
    - config: Contains API configuration constants.

Environment Variables:
    OMDB_API_KEY: The API key for accessing the OMDB API.

Configuration Constants (from config module):
    API_DATABASE_BASE_URL: The base URL for the OMDB API.
    API_DATABASE_IMG_URL: The URL for fetching movie poster images.
    API_RETRY_COUNTER: The number of retry attempts for API requests.
    API_RETRY_PAUSE: The delay between retry attempts in seconds.

Usage:
    Import the desired functions and use them to fetch movie data or poster information.

Example:
    from omdb import fetch_movie, fetch_poster

    movie_data = fetch_movie("Inception")
    poster_data = fetch_poster("Inception")

Note:
    Ensure that the OMDB_API_KEY environment variable is set before using these functions.
"""

from os import getenv
from time import sleep

import requests

from config import API_DATABASE_BASE_URL, API_DATABASE_IMG_URL, API_RETRY_COUNTER, API_RETRY_PAUSE


def fetch_movie(title):
    """
    Fetches detailed movie information from the OMDB API.

    This function attempts to retrieve movie data for the given title. It implements
    a retry mechanism to handle connection errors and timeouts.

    Args:
       title (str): The title of the movie to fetch information for.

    Returns:
       dict: A dictionary containing the movie information returned by the OMDB API.

    Raises:
       ConnectionError: If the function fails to connect to the API after all retry attempts.
       ValueError: If the movie title is not found in the OMDB database.

    Note:
       - The function uses the OMDB_API_KEY environment variable for authentication.
       - It retries the API call up to API_RETRY_COUNTER times with API_RETRY_PAUSE seconds between attempts.
    """
    request_url = f"{API_DATABASE_BASE_URL}?apikey={getenv("OMDB_API_KEY")}"
    retry_counter = 0

    while retry_counter < API_RETRY_COUNTER:
        try:
            res = requests.get(url=f"{request_url}&t={title}")
        except ConnectionError:
            retry_counter += 1
            print(
                f"Error connecting to the API, retrying in {API_RETRY_PAUSE} seconds ..."
            )
            sleep(API_RETRY_PAUSE)
            continue
        except TimeoutError:
            retry_counter += 1
            print(
                f"Error fetching data from the API (timeout), retrying in {API_RETRY_PAUSE} seconds ..."
            )
            sleep(API_RETRY_PAUSE)
            continue

        if retry_counter == API_RETRY_COUNTER:
            raise ConnectionError("Could not fetch data from the API.")

        res_json = res.json()

        if res_json["Response"] == "False":
            raise ValueError(f"Couldn't find movie {title}")

        return res_json


# yet to use, currently sits here as placeholder for potential future use in movie-app v3.
def fetch_poster(title):
    request_url = f"{API_DATABASE_IMG_URL}?apikey={getenv("OMDB_API_KEY")}"
    res = requests.get(url=f"{request_url}&t={title}")
    return res.json()
