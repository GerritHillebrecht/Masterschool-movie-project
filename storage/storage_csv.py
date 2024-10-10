from storage.iStorage import IStorage
from utility import create_movie_key
from config import SUPPORTED_MOVIE_DATA, STORAGE_CSV_SEPERATOR_SYMBOL

"""
This is slightly different from the given task, read the docstring for iStorage for clarification.
"""


class StorageCSV(IStorage):
    """
    Creates a Storage-class-instance with jscsvon specifications.
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
