from json import dumps, loads

from storage.iStorage import IStorage

"""
This is slightly different from the given task, read the docstring for iStorage for clarification.
"""


class StorageJson(IStorage):
    """
    Creates a Storage-class-instance with json specifications.
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
