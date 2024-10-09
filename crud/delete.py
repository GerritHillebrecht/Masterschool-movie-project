from storage import IStorage


def delete_movie(storage: IStorage) -> None:
    """
    Prompts the user for a movie name. Checks if the database has a movie that matches the prompt.
    Loops the prompt until a movie is found or the user exits. Updates the database accordingly.
    """
    while True:
        movie_title = input("Enter movie name to delete ('Exit' to abort): ")

        if not movie_title:
            print("Enter a movie title.")
            continue

        if movie_title.lower() == "exit":
            return

        storage.delete_movie(movie_title)
        print(f"{movie_title} successfully deleted from storage.")
        return
