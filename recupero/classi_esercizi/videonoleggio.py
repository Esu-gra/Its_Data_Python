class Movie:
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self):
        if self.is_rented:
            print(f"Il film '{self.title}' è già noleggiato.")
        else:
            self.is_rented = True

    def return_movie(self):
        if not self.is_rented:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")
        else:
            self.is_rented = False


class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie):
        if movie.is_rented:
            print(f"Il film '{movie.title}' è già noleggiato.")
        else:
            movie.rent()
            self.rented_movies.append(movie)

    def return_movie(self, movie: Movie):
        if movie not in self.rented_movies:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
        else:
            movie.return_movie()
            self.rented_movies.remove(movie)


class VideoRentalStore:
    def __init__(self):
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies:
            print(f"Il film con ID '{movie_id}' esiste già.")
        else:
            self.movies[movie_id] = Movie(movie_id, title, director)

    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")
        else:
            self.customers[customer_id] = Customer(customer_id, name)

    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id not in self.customers or movie_id not in self.movies:
            print("Cliente o film non trovato.")
        else:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)

    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id not in self.customers or movie_id not in self.movies:
            print("Cliente o film non trovato.")
        else:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id not in self.customers:
            print("Cliente non trovato.")
            return []
        return self.customers[customer_id].rented_movies

          
store = VideoRentalStore()

store.add_movie("001", "Inception", "Christopher Nolan")
store.add_movie("002", "Matrix", "Wachowski")

store.register_customer("C001", "Alice")

store.rent_movie("C001", "001")  # Alice noleggia Inception
store.rent_movie("C001", "001")  # Tentativo doppio → messaggio d'errore

store.return_movie("C001", "001")  # Alice restituisce Inception

