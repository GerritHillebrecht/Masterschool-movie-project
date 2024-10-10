from storage import IStorage, StorageJson, StorageCSV
from os import getcwd, path
from config import STORAGE_PATHS


class User:
    __slots__ = ("_name", "_storage")

    def __init__(self, name):
        self._name = name
        self._storage = StorageCSV(
            directory=str(path.join(
                getcwd(),
                STORAGE_PATHS["base"],
                STORAGE_PATHS["csv"]
            )),
            file_name=name
        )

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, new_storage):
        if not isinstance(new_storage, IStorage):
            raise TypeError("Provide a proper Storage instance")

        self._storage = new_storage
