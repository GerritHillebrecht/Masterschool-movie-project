from dotenv import load_dotenv

from app import MovieApp
from config import WELCOME_MESSAGE
from user import User, select_user

load_dotenv()


def main() -> None:
    """
    Welcomes the user and starts the command prompt-loop.
    """

    # Inform the user that the program is running by sending a welcome-message.
    print(WELCOME_MESSAGE)

    # Select the user
    username = select_user()
    user = User(name=username)

    # Instantiate Movie App and start it with selected user.
    MovieApp(user).start()


if __name__ == "__main__":
    main()
