## 🎬 Historical Film Archive Management System

A **Python program** to store, update, and manage **classic and historical films**.  
Regular users can view public movies, while researchers can access archived films after authentication.

The **Historical Film Archive Management System** is a Python-based application designed to preserve and manage a collection of classic and historical movies. It offers **role-based access**, allowing regular users to explore publicly available films, while authenticated researchers can view and update archived films—ensuring the legacy of timeless cinema is securely maintained.

---

### 📌 Features

- **Add Films** – Store new films with title, director, release year, and archive status.  
- **Delete Films** – Remove films by ID.  
- **Update Films** – Modify details such as title, director, release year, and archive status.  
- **Categorize Films**:
  - Normal Movies – Visible to all users.  
  - Archived Movies – Visible only to authenticated researchers.  
- **Researcher Management**:
  - Add and delete researchers.  
  - Authenticate researchers with username & password.  
- **Retrieve Film Details** by film ID.  
---
### 📈 Keywords (SEO)
* Historical Film Archive · Classic Film Database · Vintage Movie Collection ·
* Film Archive Management System · Movie Cataloging in Python · Movie Database Application ·
* Digital Film Preservation · Cinema History Research · Archived Movie Access
---
### 👥 User Roles

### 1️⃣ Regular User
- Can view only normal (non-archived) movies.

### 2️⃣ Researcher
- Must authenticate with a username and password.  
- Can view and manage archived films.

---

## 📂 Classes Overview

### 🎬 Film
Represents a single film in the archive.  
**Attributes:**
- `film_id` (int)  
- `title` (str)  
- `director` (str)  
- `release_year` (int)  
- `archived` (bool, default `False`)  

---

### 🗂 FilmArchive
Handles film and researcher operations:  
- `add_film(film)`  
- `delete_film(film_id)`  
- `update_film(film_id, updated_data)`  
- `get_film_details(film_id)`  
- `add_researcher(researcher)`  
- `delete_researcher(researcher_id)`  
- `authenticate_researcher(name, password)`  
- `get_normal_movies()`  
- `get_archived_movies()`  

---

### 👨‍🔬 Researcher
Represents a researcher.  
**Attributes:**
- `id` (str)  
- `name` (str)  
- `password` (str)  

---

## 🔒 Authentication
Only researchers with the correct **username** and **password** can view archived films.

---

### 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Anujashirahatti/film-archive.git
cd film-archive


