from abc import ABC, abstractmethod
from os import path

"""
I don't see why we need an abstract class for this, since this mainly creates duplicate
code (double crud functions). You can just have filepath and filetype as parameters of the init function.
Changed the layout, so we have abstract methods for the read and write functions instead.

This will be used as an extension of the user-class, so we can call the storage functions
directly from the user and initialize it with the correct user data. 
"""


# Naming interfaces with a leading "i" is outdated btw.
class IStorage(ABC):
    __slots__ = ("_directory", "_file_extension", "_user", "_file_path")

    def __init__(
            self,
            directory: str,
            file_extension: str,
            user: str
    ) -> None:
        """
        Takes in the parameters needed for reading and writing to storage files.
        Done inside the parent-class, to reduce duplicate code.
        :param directory: The base-path of the directory where the data should be stored.
        :param file_extension: The file-extension, only "json" and "csv" are currently supported
        :param user: The filename this is saved to. E.g. the username or the uuid.
        """
        self._directory = directory
        self._file_extension = file_extension
        self._user = user
        self._file_path = str(path.join(self._file_path, f"{self._user}.{self._file_extension}"))

        self._create_file_if_not_exists()

    def list_movies(self) -> list[dict]:
        """ Returns the list of movies saved in the storage. """
        return self._read_from_file()

    def add_movie(self, title: str, year: int, rating: int | float, poster: str) -> None:
        """ Adds a movie to the database. """

        if not isinstance(title, str):
            raise TypeError("The title should be of type string.")

        if not isinstance(year, int):
            raise TypeError("Please provide the year of release as an integer.")

        if not isinstance(rating, (int, float)):
            raise TypeError("Please provide a rating as integer or float")

        if not isinstance(poster, str):
            raise TypeError("Please provide a poster-url as a string.")

        if not title or not year or not rating or not poster:
            raise ValueError("Please provide all the needed data about the movie.")

        movies_in_storage = self._read_from_file()
        new_movie = {
            "title": title,
            "year": year,
            "rating": rating,
            "poster": poster
        }

        self._write_to_file(movies_in_storage + [new_movie])

    def delete_movie(self, title: str) -> list[dict]:
        """
        Delete a movie from the storage.
        :param title: The title of the movie.
        :return: The movies in the storage after deletion.
        """
        movies_in_storage = self._read_from_file()
        movie_exists = bool(next(
            (movie for movie in movies_in_storage),
            None
        ))

        if not movie_exists:
            raise ValueError("Movie not found in the storage.")

        filtered_movies = [
            movie
            for movie in movies_in_storage
            if movie.get("title", "") != title
        ]

        self._write_to_file(filtered_movies)

        return filtered_movies

    def update_movie(self, title, rating) -> dict:
        """
        Updates the rating of a movie.
        :param title: The title of the movie to be updated. Must be precise.
        :param rating: The new rating of the movie.
        :return: The updated movie data.
        """
        movies_in_storage = self._read_from_file()
        movie = next(
            movie
            for movie in movies_in_storage
            if movie.get("title", "") == title
        )

        if not movie:
            raise ValueError("Movie not found in the storage.")

        movie["rating"] = rating

        self._write_to_file(movies_in_storage)

        return movie

    @abstractmethod
    def _read_from_file(self) -> list[dict]:
        pass

    @abstractmethod
    def _write_to_file(self, content: list) -> list[dict]:
        pass

    def _create_file_if_not_exists(self):
        # checks if file exits, creates it otherwise.
        if not path.exists(self._file_path):
            open(self._file_path, "x")
