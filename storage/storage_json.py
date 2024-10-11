from json import dumps, loads

from storage.iStorage import IStorage

"""
This is slightly different from the given task, read the docstring for iStorage for clarification.
"""


class StorageJson(IStorage):
    """
    StorageJson Class

    This class implements the IStorage abstract base class for JSON-based storage operations
    in a movie database application. It provides concrete implementations for reading from
    and writing to JSON files.

    Inherits from:
        IStorage

    Attributes:
        Inherits all attributes from IStorage

    Methods:
        __init__(directory: str, file_name: str) -> None:
            Initializes the StorageJson object with the given parameters.

        _read_from_file() -> dict[str, dict]:
            Reads data from the JSON storage file.

        _write_to_file(content: dict[str, dict]) -> dict[str, dict]:
            Writes data to the JSON storage file.

    Note:
        This class uses the built-in json module for serialization and deserialization of data.
        The file extension is automatically set to "json" in the constructor.
    """
    def __init__(
            self,
            directory: str,
            file_name: str
    ) -> None:
        """
        Calls the super function to initialize the parent-class-data. Specifies the
        file_extension as "json".
        :param directory: The base-directory of the storage.
        :param file_name: The file-name of the storage, e.g. username or uuid.
        """
        super().__init__(
            directory=directory,
            file_extension="json",
            file_name=file_name
        )

    def _read_from_file(self) -> dict[str, dict]:
        """
        Loads the data from the user-file.
        File existence is checked upon initialization of the class.
        """

        with open(self._file_path, "r") as handle:
            storage_data = handle.read()
            return loads(storage_data) if len(storage_data) > 0 else {}

    def _write_to_file(self, content: dict[str, dict]) -> dict[str, dict]:
        """
        Writes to specified user-file.
        File existence is checked upon initialization of the class.
        """

        # open the file and write the content to it.
        with open(self._file_path, "w") as handle:
            handle.write(dumps(content))

        # Reread the content from the storage for testability.
        return self._read_from_file()
