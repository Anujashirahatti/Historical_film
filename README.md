🎬 Film Archive Management System
A Python program for managing a collection of films, designed for both regular users and researchers.
It supports adding, deleting, updating, and categorizing films into normal and archived. Researchers can authenticate to view archived films.

📌 Features
Add Films to the archive.
Delete Films by ID.
Update Film Details (title, director, release year, archived status).

Categorize Films:
Normal Movies (visible to all users)
Archived Movies (visible only to authenticated researchers)
Researcher Management:

Add and delete researchers.
Authenticate researchers with a username and password.
Retrieve Film Details by ID.

🏗️ Project Structure
plaintext
Copy
Edit
FilmArchive/
│
├── main.py               # Main program file (contains all classes and logic)
├── README.md              # Project documentation
└── requirements.txt       # (Optional) Dependencies, if any
🚀 How to Run
Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-Anujashirahatti/film-archive.git
cd film-archive
Run the Program

bash
Copy
Edit
python main.py
Follow the Prompts

Choose whether you are a user or researcher.
If researcher, provide valid credentials.
View movies according to your role.
Optionally update a movie's details.

👥 User Roles
1️⃣ Regular User
Can view normal movies (not archived).

2️⃣ Researcher
Must authenticate with name and password.

Can view archived movies.
Are you a regular user or a researcher? (Type 'user' or 'researcher'): user
Normal Movies:
Title: managal_pandey, Director: ketan_mehta, Release Year: 2001
Title: padmaavat, Director: leela_bhansali, Release Year: 2018
...
Enter the ID of the movie you want to update: 5
Enter updated title: Padmaavat
Enter updated director: Sanjay Leela Bhansali
Enter updated release year: 2018
Is the movie archived? (True/False): false
📂 Classes Overview
Film
Represents a single film in the archive.

Attributes:
film_id (int)
title (str)
director (str)
release_year (int)
archived (bool, default False)

FilmArchive
Handles film and researcher operations:
add_film(film)
delete_film(film_id)
update_film(film_id, updated_data)
get_film_details(film_id)
add_researcher(researcher)
delete_researcher(researcher_id)

authenticate_researcher(name, password)
get_normal_movies()
get_archived_movies()
Researcher
Represents a researcher.

Attributes:
id (str)
name (str)
password (str)

🔒 Authentication
Only researchers with correct name and password can view archived films.
