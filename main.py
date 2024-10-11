"""
Movie Application Main Module

This module serves as the entry point for a movie application. It handles user selection,
initializes the main application, and starts the program.

The module performs the following tasks:
1. Loads environment variables from a .env file
2. Displays a welcome message to the user
3. Prompts the user to select or create a user profile
4. Initializes and starts the main MovieApp with the selected user

Dependencies:
- dotenv: For loading environment variables
- app: Contains the MovieApp class
- config: Contains the WELCOME_MESSAGE constant
- user: Contains the User class and select_user function

Usage:
Run this script directly to start the movie application.

"""

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
