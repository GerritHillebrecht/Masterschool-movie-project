from storage import IStorage, StorageJson, StorageCSV
from os import getcwd, path
from config import STORAGE_PATHS
from json import loads, dumps

user_file = f"{path.join(
    getcwd(),
    "user",
    "user-management"
)}.json"


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
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name or not isinstance(new_name, str):
            raise ValueError("Please provide a valid name.")

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, new_storage):
        if not isinstance(new_storage, IStorage):
            raise TypeError("Provide a proper Storage instance")

        self._storage = new_storage


def select_user() -> str:
    users = load_users_from_storage()

    # Print selectable Users
    for idx, user in enumerate(users):
        print(f'{idx + 1}. {user["name"]}')

    print(f"{len(users) + 1}. Create new user")

    user = prompt_user(users)

    return user["name"]


def prompt_user(users: list[dict]) -> dict:
    while True:
        try:
            user = int(input("Select a user (by number): "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if not 1 <= user <= (len(users) + 1):
            print("Please select a number within range")
            continue

        if user <= len(users):
            return users[user - 1]

        return add_user_to_storage(users)


def load_users_from_storage() -> list[dict]:
    if not path.exists(user_file):
        open(user_file, "x")

    with open(user_file, "r") as handle:
        storage_data = handle.read()
        users = loads(storage_data) if len(storage_data) > 0 else []

    return users


def add_user_to_storage(users: list[dict]) -> dict:
    username = prompt_username()

    # extendable to preferred storage-type for example.
    user = {
        "name": username
    }

    with open(user_file, "w") as handle:
        users.append(user)
        handle.write(dumps(users))

    return user


def prompt_username():
    while True:
        username = input("What is your name? ")

        if not username:
            print("Please enter a valid username")
            continue

        return username
