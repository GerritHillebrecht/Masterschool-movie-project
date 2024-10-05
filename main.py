from config import WELCOME_MESSAGE
from dispatcher import dispatcher
from start_loop import start


def main() -> None:
    """
    Welcomes the user and starts the command prompt-loop.
    """
    # Inform the user that the program is running by sending a welcome-message.
    print(WELCOME_MESSAGE)

    # Get and pass all available user-commands to the loop-starting-function.
    start(dispatcher)


if __name__ == "__main__":
    main()
