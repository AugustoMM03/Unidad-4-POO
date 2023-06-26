import requests


class Pelicula(object):
    __title : str
    __overview : str
    __language : str
    __date : str 
    __genres : str

    def __init__(self, tit, ov, lang, date, gen):
        self.__title = tit
        self.__overview = ov
        self.__language = lang
        self.__date = date
        self.__genres = gen

    def getTitle(self):
        return self.__title
    
    def getOverView(self):
        return self.__overview
    
    def getLanguage(self):
        return self.__language
    
    def getDate(self):
        return self.__date
    
    def getGenres(self):
        return self.__genres

class ManejadorPeliculas(object):
    indice = 0
    __peliculas = None

    def __init__(self):
        self.__peliculas = []

    def agregarPelicula(self, pelicula):
        self.__peliculas.append(pelicula)

    def getListaPeliculas(self):
        return self.__peliculas
    

class RepositorioPeliculas(object):
    __apikey = None
    __manejador = None
    __url = None

    def __init__(self):
        self.__apikey = '3d84c4afb22d8a8cbaa4662126626b18'
        self.__url = f'https://api.themoviedb.org/3/discover/movie?api_key={self.__apikey}'
        self.__manejador = ManejadorPeliculas()

    def obtenerPeliculas(self):
        response = requests.get(self.__url)
        if response.status_code == 200:
            data = response.json()
            peliculas = data['results']
            return peliculas
        else:
            return []

    def obtenerGeneros(self, idgenero):
        url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={self.__apikey}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            genres = data['genres']
            for genre in genres:
                if genre['id'] == idgenero:
                    return genre['name']
        return 'Desconocido'

    def crearPeliculas(self, peliculas):

        for pelicula in peliculas:
            title = pelicula['title']
            overview = pelicula['overview']
            lang = pelicula['original_language']
            date = pelicula ['release_date']
            genres = pelicula ['genre_ids']
            nombres_generos = [self.obtenerGeneros(genero) for genero in genres]
            instancia = Pelicula(title,overview,lang,date,nombres_generos)
            self.__manejador.agregarPelicula(instancia)
        return self.__manejador
