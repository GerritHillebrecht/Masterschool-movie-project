from storage import IStorage
from os import path, getcwd
from config import MAX_RATING
import webbrowser


def generate_website(storage: IStorage):
    """
    Takes in the storage and creates a website based on the template and the data from the storage.
    :param storage: The storage instance to base the website on.
    """
    grid = generate_movie_grid(storage.list_movies())

    base_path = path.join(getcwd(), "web_gen", "template")
    template_path = path.join(base_path, "index_template.html")
    output_path = path.join(base_path, "output.html")
    username = storage.file_name

    with open(template_path, "r") as handle:
        template = handle.read()
        template = template.replace("__TEMPLATE_TITLE__", "Fantastic IMDB ripoff")
        template = template.replace("__TEMPLATE_MOVIE_GRID__", grid)
        template = template.replace("__TEMPLATE_USER__", username)

    if not path.exists(output_path):
        open(output_path, "x")

    with open(output_path, "w") as handle:
        handle.write(template)

    webbrowser.open(output_path)
    print("Website was generated successfully")


def generate_movie_grid(movies: dict[str, dict]) -> str:
    """
    Creates a grid representing the movies for the website.
    :param movies: The movies to represent.
    :return: A string of HTML-data
    """

    return "".join(
        f"""
        <li>
            <a href="https://www.imdb.com/title/{movie.get("imdbID")}" target="_blank" title="{movie.get("notes") or ""}" class="movie">
                <div class="rating">{movie["rating"]} / {MAX_RATING}</div>
                <div class="countries">
                    {
                        "".join(
                            f'<img width="20" src="https://flagcdn.com/w20/{country_code.lower()}.png" />'
                            for country_code in movie["country_codes"]
                            if country_code
                        )
                    }
                </div>
                <img class="movie-poster" src="{movie["poster"]}" alt="{movie["title"]}">
                <div class="movie-title">{movie["title"]}</div>
                <div class="movie-year">{movie["year"]}</div>
            </a>
        </li>
        """
        for movie in movies.values()
    )
