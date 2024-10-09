from config import MAX_RATING
from dispatcher import dispatcher
from user import User


class MovieApp:
    __slots__ = ("_user", "_dispatcher")

    def __init__(self, user: User):
        self._user = user
        self._dispatcher = dispatcher

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, new_user):
        if not isinstance(new_user, User):
            raise TypeError("Please provide a correct user.")

        self._user = new_user

    def start(self):
        """
        Starts the app by repeatedly prompting the user for commands until ended by user.
        """

        # Print available commands
        self._print_menu()

        # Prompt commands
        self._prompt_command()

    def _print_menu(self):
        # Start-up menu.
        print("Menu:\n0. Exit")
        for idx, (label, command) in enumerate(self._dispatcher.items()):
            print(f'{idx + 1}. {command["name"]}')

    def _prompt_command(self):
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
