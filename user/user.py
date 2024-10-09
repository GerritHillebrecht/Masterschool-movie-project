from storage import StorageJson
from os import getcwd, path
from config import STORAGE_PATHS


class User:
    __slots__ = ("_name", "_storage")

    def __init__(self, name):
        self._name = name
        self._storage = StorageJson(
            directory=str(path.join(
                getcwd(),
                STORAGE_PATHS["base"],
                STORAGE_PATHS["json"]
            )),
            file_name=name
        )

    @property
    def storage(self):
        return self._storage
