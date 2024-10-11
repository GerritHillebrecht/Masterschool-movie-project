import requests

from time import sleep
from os import getenv
from config import API_DATABASE_BASE_URL, API_DATABASE_IMG_URL, API_RETRY_COUNTER, API_RETRY_PAUSE


def fetch_movie(title):
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


def fetch_poster(title):
    request_url = f"{API_DATABASE_IMG_URL}?apikey={getenv("OMDB_API_KEY")}"
    res = requests.get(url=f"{request_url}&t={title}")
    return res.json()
