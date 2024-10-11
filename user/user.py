"""
User Management Module

This module provides functionality for managing users in a movie database application.
It includes a User class for representing individual users and functions for user selection,
creation, and storage management.

Classes:
    User: Represents a user with a name and associated storage.

Functions:
    select_user() -> str:
        Prompts the user to select or create a user and returns the selected username.

    prompt_user(users: list[dict]) -> dict:
        Handles user input for selecting or creating a user.

    load_users_from_storage() -> list[dict]:
        Loads the list of users from the storage file.

    add_user_to_storage(users: list[dict]) -> dict:
        Adds a new user to the storage file.

    prompt_username() -> str:
        Prompts for and returns a valid username.

Constants:
    user_file (str): The path to the JSON file storing user data.

Dependencies:
    - storage module: For IStorage, StorageJson, and StorageCSV classes
    - os module: For file path operations
    - json module: For JSON serialization and deserialization
    - config module: For storage path configurations
"""

from json import loads, dumps
from os import getcwd, path

from config import STORAGE_PATHS
from storage import IStorage, StorageJson

user_file = f"{path.join(
    getcwd(),
    "user",
    "user-management"
)}.json"


class User:
    """
    Represents a user in the movie database application.

    This class encapsulates user information and associated storage operations.

    Attributes:
        _name (str): The name of the user.
        _storage (IStorage): The storage instance associated with the user.

    Properties:
        name (str): Gets or sets the user's name.
        storage (IStorage): Gets or sets the user's storage instance.
    """
    __slots__ = ("_name", "_storage")

    def __init__(self, name):
        """
        Initializes a User instance.

        Args:
            name (str): The name of the user.
        """
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
        """Gets the user's name."""
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Sets the user's name.

        Args:
            new_name (str): The new name for the user.

        Raises:
            ValueError: If the new name is invalid or empty.
        """
        if not new_name or not isinstance(new_name, str):
            raise ValueError("Please provide a valid name.")

    @property
    def storage(self):
        """Gets the user's storage instance."""
        return self._storage

    @storage.setter
    def storage(self, new_storage):
        """
        Sets the user's storage instance.

        Args:
            new_storage (IStorage): The new storage instance for the user.

        Raises:
            TypeError: If the new storage is not an instance of IStorage.
        """
        if not isinstance(new_storage, IStorage):
            raise TypeError("Provide a proper Storage instance")

        self._storage = new_storage


def select_user(username: str | None) -> str:
    """
    Prompts the user to select an existing user or create a new one.

    Returns:
        str: The name of the selected or created user.
    """
    users = load_users_from_storage()

    if username:
        if username not in set(user["name"] for user in users):
            add_user_to_storage(username, users)

        return username
    # Print selectable Users
    for idx, user in enumerate(users):
        print(f'{idx + 1}. {user["name"]}')

    print(f"{len(users) + 1}. Create new user")

    user = prompt_user(users)

    return user["name"]


def prompt_user(users: list[dict]) -> dict:
    """
    Handles user input for selecting an existing user or creating a new one.

    Args:
        users (list[dict]): List of existing users.

    Returns:
        dict: The selected or newly created user dictionary.
    """

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

        return add_user_to_storage(prompt_username(), users)


def load_users_from_storage() -> list[dict]:
    """
    Loads the list of users from the storage file.

    Returns:
        list[dict]: A list of dictionaries containing user information.
    """
    if not path.exists(user_file):
        open(user_file, "x")

    with open(user_file, "r") as handle:
        storage_data = handle.read()
        users = loads(storage_data) if len(storage_data) > 0 else []

    return users


def add_user_to_storage(username: str, users: list[dict]) -> dict:
    """
    Adds a new user to the storage file.

    Args:
        users (list[dict]): The current list of users.

    Returns:
        dict: The newly created user dictionary.
    """

    # extendable to preferred storage-type for example.
    user = {
        "name": username
    }

    with open(user_file, "w") as handle:
        users.append(user)
        handle.write(dumps(users))

    return user


def prompt_username():
    """
    Prompts the user to enter a valid username.

    Returns:
        str: A non-empty username string.
    """
    while True:
        username = input("What is your name? ")

        if not username:
            print("Please enter a valid username")
            continue

        return username
