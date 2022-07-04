from domain.movie import Movie
from service.film_manager import FilmManager

option = None

while option != 4:
    print("""
    1. Add Movie
    2. Movie List
    3. Delete Movies
    4. Exit
    """)
    try:
        option = int(input("Choose an option: "))
    except Exception as e:
        print(f"An  error has ocurred: {e}")

    if option == 1:
        movie_name = input("Name of the movie: ")
        movie = Movie(movie_name)
        FilmManager.add_movie(movie)
    elif option == 2:
        FilmManager.movie_list()
    elif option == 3:
        FilmManager.remove_film_manager()
    else:
        print("Please, choose a correct option")
    