from os import path
from config import WELCOME_MESSAGE, STORAGE_PATHS
from dispatcher import dispatcher
from start_loop import start
from storage.storage_json import StorageJson


def main() -> None:
    """
    Welcomes the user and starts the command prompt-loop.
    """
    storage_json = StorageJson(
        directory=str(path.join(
            STORAGE_PATHS["base"],
            STORAGE_PATHS["json"]
        )),
        file_name="Gerrit"
    )

    # Inform the user that the program is running by sending a welcome-message.
    print(WELCOME_MESSAGE)
    try:
        storage_json.add_movie(
            title="Joker",
            year=2024,
            rating=8,
            poster="ASD"
        )
    except ValueError:
        print("Already in storage")

    # Get and pass all available user-commands to the loop-starting-function.
    start(dispatcher)


if __name__ == "__main__":
    main()
