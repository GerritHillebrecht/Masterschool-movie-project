from storage import IStorage
from os import path, getcwd
import webbrowser


def generate_website(storage: IStorage):
    grid = generate_movie_grid(storage.list_movies())

    base_path = path.join(getcwd(), "web_gen", "template")
    template_path = path.join(base_path, "index_template.html")
    output_path = path.join(base_path, "output.html")

    with open(template_path, "r") as handle:
        template = handle.read()
        template = template.replace("__TEMPLATE_TITLE__", "Fantastic IMDB ripoff")
        template = template.replace("__TEMPLATE_MOVIE_GRID__", grid)

    if not path.exists(output_path):
        open(output_path, "x")

    with open(output_path, "w") as handle:
        handle.write(template)

    webbrowser.open(output_path)
    return grid


def generate_movie_grid(movies: dict[str, dict]):
    return "".join(
        f"""
        <li>
            <img class="movie-poster" src="{movie["poster"]}" alt="{movie["title"]}">
            <div class="movie-title">{movie["title"]}</div>
            <div class="movie-year">{movie["year"]}</div>
        </li>
        """
        for movie in movies.values()
    )
