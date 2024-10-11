from storage.iStorage import IStorage
from utility import create_movie_key
from config import SUPPORTED_MOVIE_DATA, STORAGE_CSV_SEPERATOR_SYMBOL

"""
This is slightly different from the given task, read the docstring for iStorage for clarification.
"""


class StorageCSV(IStorage):
    """
    StorageCSV Class

    This class implements the IStorage abstract base class for CSV-based storage operations
    in a movie database application. It provides concrete implementations for reading from
    and writing to CSV files, as well as methods for converting between CSV and dictionary formats.

    Inherits from:
        IStorage

    Attributes:
        _csv_separator (str): The separator symbol used in the CSV file.

    Methods:
        __init__(directory: str, file_name: str, csv_separator: str = STORAGE_CSV_SEPERATOR_SYMBOL) -> None:
            Initializes the StorageCSV object with the given parameters.

        _read_from_file() -> dict[str, dict]:
            Reads data from the CSV storage file.

        _write_to_file(content: dict[str, dict]) -> dict[str, dict]:
            Writes data to the CSV storage file.

        _convert_from_storage(lines: list[str]) -> dict[str, dict]:
            Converts CSV lines to a dictionary of movie data.

        _convert_to_storage(movies: dict[str, dict]) -> str:
            Converts a dictionary of movie data to CSV format.

    Note:
        This class uses a custom CSV format where each line represents a movie,
        and values are separated by the specified CSV separator.
        The file extension is automatically set to "csv" in the constructor.
    """
    __slots__ = "_csv_seperator"

    def __init__(
            self,
            directory: str,
            file_name: str,
            csv_seperator=STORAGE_CSV_SEPERATOR_SYMBOL
    ) -> None:
        """
        Calls the super function to initialize the parent-class-data. Specifies the
        file_extension as "csv".
        :param directory: The base-directory of the storage.
        :param file_name: The file-name of the storage, e.g. username or uuid.
        """
        self._csv_seperator = csv_seperator

        super().__init__(
            directory=directory,
            file_extension="csv",
            file_name=file_name
        )

    def _read_from_file(self) -> dict[str, dict]:
        """
        Loads the data from the user-file.
        File existence is checked upon initialization of the class.
        """

        with open(self._file_path, "r") as handle:
            return self._convert_from_storage(handle.readlines())

    def _write_to_file(self, content: dict[str, dict]) -> dict[str, dict]:
        """
        Writes to specified user-file.
        File existence is checked upon initialization of the class.
        """

        with open(self._file_path, "w") as handle:
            handle.write(self._convert_to_storage(content))

        # Reread the content from the storage for testability.
        return self._read_from_file()

    def _convert_from_storage(self, lines) -> dict[str, dict]:
        """
        Converts the data from the storage into usable data as a list of dictionaries.
        :param lines: All lines read from the database-file.
        :return: Returns a list of dictionaries representing the movies.
        """
        return {
            create_movie_key(
                line[0]
            ): {
                # Reads the data structure from the config-file
                SUPPORTED_MOVIE_DATA[idx]["name"]: value
                # Strips all trailing " " and "\n". Splits by the storage seperator-symbol from the config-file.
                for idx, value in enumerate(line)
            }
            for line in map(
                lambda line: line.strip().split(self._csv_seperator),
                lines
            )
        }

    def _convert_to_storage(self, movies: dict[str, dict]) -> str:
        """
        Converts the list of dictionaries format for movies to work with back into lines for the .csv database.
        :param movies: The movies to be converted.
        :return: Returns writeable data for the database.
        """
        return "\n".join(
            self._csv_seperator.join(str(val) for val in movie.values())
            for movie in movies.values()
        )
