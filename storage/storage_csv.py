from storage.iStorage import IStorage
from config import SUPPORTED_MOVIE_DATA, STORAGE_CSV_SEPERATOR_SYMBOL

"""
This is slightly different from the given task, read the docstring for iStorage for clarification.
"""


class StorageCSV(IStorage):
    """
    Creates a Storage-class-instance with jscsvon specifications.
    """

    def __init__(
            self,
            directory: str,
            file_name: str
    ) -> None:
        """
        Calls the super function to initialize the parent-class-data. Specifies the
        file_extension as "csv".
        :param directory: The base-directory of the storage.
        :param file_name: The file-name of the storage, e.g. username or uuid.
        """
        super().__init__(
            directory=directory,
            file_extension="csv",
            file_name=file_name
        )

    def _read_from_file(self) -> list[dict]:
        """
        Loads the data from the user-file.
        File existence is checked upon initialization of the class.
        """

        with open(self._file_path, "r") as handle:
            return self._convert_from_storage(handle.readlines())

    def _write_to_file(self, content: list[dict]) -> list[dict]:
        """
        Writes to specified user-file.
        File existence is checked upon initialization of the class.
        """

        with open(self._file_path, "w") as handle:
            handle.write(self._convert_to_storage(content))

        # Reread the content from the storage for testability.
        return self._read_from_file()

    def _convert_from_storage(self, lines) -> list[dict]:
        """
        Converts the data from the storage into usable data as a list of dictionaries.
        :param lines: All lines read from the database-file.
        :return: Returns a list of dictionaries representing the movies.
        """
        return [
            {
                # Reads the data structure from the config-file
                SUPPORTED_MOVIE_DATA[idx]["name"]: value
                # Strips all trailing " " and "\n". Splits by the database seperator-symbol from the config-file.
                for idx, value in enumerate(line.strip().split(STORAGE_CSV_SEPERATOR_SYMBOL))
            }
            for line in lines
        ]

    def _convert_to_storage(self, movies: list[dict]) -> str:
        """
        Converts the list of dictionaries format for movies to work with back into lines for the .csv database.
        :param movies: The movies to be converted.
        :return: Returns writeable data for the database.
        """
        return "".join(
            [
                STORAGE_CSV_SEPERATOR_SYMBOL.join([str(val) for val in movie.values()]) + "\n"
                for movie in movies
            ]
        )
