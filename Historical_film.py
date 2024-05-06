class Film:
    def __init__(self, film_id, title, director, release_year, archived=False):
        self.film_id = film_id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.archived = archived

class FilmArchive:
    def __init__(self):
        self.film_records = []
        self.researchers = []

    def add_film(self, film):
        self.film_records.append(film)

    def delete_film(self, film_id):
        for film in self.film_records:
            if film.film_id == film_id:
                self.film_records.remove(film)
                break
        else:
            print(f"Film with ID {film_id} not found in the archive.")

    def update_film(self, film_id, updated_data):
        for film in self.film_records:
            if film.film_id == film_id:
                film.title = updated_data.title
                film.director = updated_data.director
                film.release_year = updated_data.release_year
                break
        else:
            print(f"Film with ID {film_id} not found in the archive.")

    def get_film_details(self, film_id):
        for film in self.film_records:
            if film.film_id == film_id:
                return f"Film ID: {film.film_id}\nTitle: {film.title}\nDirector: {film.director}\nRelease Year: {film.release_year}"
        return f"Film with ID {film_id} not found in the archive."

    def add_researcher(self, researcher):
        self.researchers.append(researcher)

    def delete_researcher(self, researcher_id):
        for researcher in self.researchers:
            if researcher.id == researcher_id:
                self.researchers.remove(researcher)
                break
        else:
            print(f"Researcher with ID {researcher_id} not found.")

    def authenticate_researcher(self, name, password):
        for researcher in self.researchers:
            if researcher.name == name and researcher.password == password:
                return True
        return False

    def get_normal_movies(self):
        return [film for film in self.film_records if not film.archived]

    def get_archived_movies(self):
        return [film for film in self.film_records if film.archived]

class Researcher:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

archive = FilmArchive()
archive.add_film(Film(1, "Casablanca", "Michael Curtiz", 1942))
archive.add_film(Film(2, "Gone with the Wind", "Victor Fleming", 1939, True))
archive.add_film(Film(3,"kesari","Anurag_singh",2019, True))
archive.add_film(Film(4,"managal_pandey","ketan_mehta",2001))
archive.add_film(Film(5,"padmaavat","leela_bhansali",2018))
archive.add_film(Film(6,"Bhahubali","raja_murali",2015))
archive.add_film(Film(7,"Bajirao_mastani","sanjay_leela",2015))

researcher1 = Researcher("6534", "anu", "password123")
researcher2= Researcher("6543", "swathi", "password321")
researcher3 = Researcher("6554", "Nayana", "password231")
researcher4=Researcher("1234","Anupama","password111")

archive.add_researcher(researcher1)
archive.add_researcher(researcher2)
archive.add_researcher(researcher3)
archive.add_researcher(researcher4)

user_type = input("Are you a regular user or a researcher? (Type 'user' or 'researcher'): ").lower()

if user_type == 'researcher':
    researcher_name = input('Enter your researcher name: ')
    researcher_password = input('Enter your researcher password: ')
    if archive.authenticate_researcher(researcher_name, researcher_password):
        print('Authentication successful! Welcome researcher.')
        archived_movies = archive.get_archived_movies()
        print("Archived Movies:")
        for film in archived_movies:
            print(f"Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}")
    else:
        print('Invalid researcher credentials.')
elif user_type == 'user':
    normal_movies = archive.get_normal_movies()
    print("Normal Movies:")
    for film in normal_movies:
        print(f"Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}")
else:
    print('Invalid user type.')
film_id_to_update = int(input("Enter the ID of the movie you want to update: "))

film_to_update = None
for film in archive.film_records:
    if film.film_id == film_id_to_update:
        film_to_update = film
        break

if film_to_update:
    updated_title = input("Enter updated title: ")
    updated_director = input("Enter updated director: ")
    updated_release_year = int(input("Enter updated release year: "))
    updated_archived = input("Is the movie archived? (True/False): ").lower() == 'true'
    updated_movie = Film(film_id_to_update, updated_title, updated_director, updated_release_year, updated_archived)

    archive.update_film(film_id_to_update, updated_movie)
else:
    print(f"Movie with ID {film_id_to_update} not found in the archive.")
    print("update_film")
