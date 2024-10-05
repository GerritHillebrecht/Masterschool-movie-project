from collections import OrderedDict


def start(dispatcher: OrderedDict[str, dict]) -> None:
    """
    Repeatedly prompts the user for commands until ended by user.
    :param dispatcher: Takes in the list of commands.
    :return: This function does not return a value.
    """
    # Start-up menu.
    print("Menu:\n0. Exit")
    for idx, (label, command) in enumerate(dispatcher.items()):
        print(f'{idx + 1}. {command["name"]}')
    print("")

    # Actual input loop.
    while True:
        try:
            selected_command = int(input(f"Enter a choice (0-{len(dispatcher)}): "))
        except ValueError:
            print("Please pass your choice as a number.")
            continue

        # len(commands) without (-1) because command 0 (exit) is not listed in the commands list.
        if not 0 <= selected_command <= len(dispatcher):
            print("Please choose one of the displayed choices")
            continue

        # Exit if user selects 0.
        if selected_command == 0:
            print("Bye!")
            return

        # Execute selected function, (-1) because "0. Exit" is not included in commands-list.
        dispatcher_label = list(label for label in dispatcher)[selected_command - 1]
        dispatcher[dispatcher_label]["function"]()
