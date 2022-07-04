import os

class FilmManager:
    
    CURRENT_PATH = os.path.dirname(__file__)
    FILE_PATH = os.path.join(CURRENT_PATH, "movies.txt")

    @classmethod
    def add_movie(cls, movie):
        with open(cls.FILE_PATH, 'a', encoding='utf-8') as file:
            file.write(f"{movie.name}\n")

    @classmethod
    def movie_list(cls):
        with open(cls.FILE_PATH, encoding='utf-8') as file:
            print(f" Film Manager ".center(50, "-"))
            print(file.read())
    
    @classmethod
    def remove_film_manager(cls):
        os.remove(cls.FILE_PATH)