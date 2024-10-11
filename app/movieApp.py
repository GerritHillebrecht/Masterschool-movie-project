"""
Movie Application Module

This module defines the MovieApp class, which serves as the main application for a movie-related program.
It handles user interaction, command dispatching, and overall application flow.

Classes:
    MovieApp: The main application class that manages user interactions and command execution.

Dependencies:
    - disp: Contains the disp object with available commands
    - user: Contains the User class

Usage:
    Create an instance of MovieApp with a User object and call the start() method to run the application.

Example:
    user = User(name="John Doe")
    app = MovieApp(user)
    app.start()
"""

from app.dispatcher import dispatcher
from user import User


class MovieApp:
    """
    The main application class for the movie program.

    This class manages user interactions, displays the command menu, and executes user-selected commands.

    Attributes:
       _user (User): The current user of the application.
       _dispatcher (dict): A dictionary containing available commands and their corresponding functions.

    Methods:
       start(): Starts the application and handles the main interaction loop.
       _print_menu(): Displays the available commands to the user.
       _prompt_command(): Prompts the user for command input and executes the selected command.
    """
    __slots__ = ("_user", "_dispatcher")

    def __init__(self, user: User):
        """
        Initializes a new MovieApp instance.

        Args:
           user (User): The user object representing the current user of the application.
        """
        self._user = user
        self._dispatcher = dispatcher

    @property
    def user(self):
        """
        Gets the current user of the application.

        Returns:
            User: The current user object.
        """
        return self._user

    @user.setter
    def user(self, new_user):
        """
        Sets a new user for the application.

        Args:
            new_user (User): The new user object to set.

        Raises:
            TypeError: If the provided new_user is not an instance of the User class.
        """
        if not isinstance(new_user, User):
            raise TypeError("Please provide a correct user.")

        self._user = new_user

    def start(self):
        """
        Starts the application by displaying the menu and entering the main command loop.

        This method initiates the application, prints the available commands, and
        repeatedly prompts the user for input until they choose to exit.
        """

        # Print available commands
        self._print_menu()

        # Prompt commands
        self._prompt_command()

    def _print_menu(self):
        """
        Displays the available commands to the user.

        This method prints a welcome message with the user's name and lists all available
        commands, including the exit option.
        """
        # Start-up menu.
        print(
            f"\nWelcome {self._user.name}"
            "\nMenu:\n0. Exit"
        )
        for idx, (label, command) in enumerate(self._dispatcher.items()):
            print(f'{idx + 1}. {command["name"]}')

    def _prompt_command(self):
        """
        Prompts the user for command input and executes the selected command.

        This method enters a loop that continuously asks the user to select a command.
        It handles input validation, executes the chosen command, and exits when the user selects '0'.
        """
        while True:
            # self._print_menu()
            try:
                selected_command = int(input(f"\nEnter a choice (0-{len(self._dispatcher)}): "))
            except ValueError:
                print("Please pass your choice as a number.")
                continue

            # len(commands) without (-1) because command 0 (exit) is not listed in the commands list.
            if not 0 <= selected_command <= len(self._dispatcher):
                print("Please choose one of the displayed choices")
                continue

            # Exit if user selects 0.
            if selected_command == 0:
                print("Bye!")
                return

            # Execute selected function, (-1) because "0. Exit" is not included in commands-list.
            dispatcher_label = list(label for label in self._dispatcher)[selected_command - 1]
            self._dispatcher[dispatcher_label]["function"](self.user.storage)
