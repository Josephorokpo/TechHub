# TechHub

Welcome to TechHub! This project is a tech blog platform where users can find and share tutorials and articles about various tech topics. 

## Features

- User authentication (sign up, log in, log out)
- Create, read, update, and delete articles
- Comment on articles
- Reply to comments
- Categories for articles
- Search functionality
- Featured articles
- Pagination for article listings

## Technologies Used

- Django
- Bootstrap
- SQLite (default, can be changed to PostgreSQL or another database)
- HTML/CSS

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/techhub.git
   cd techhub

2. Create and activate a virtual environment:

  python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.  Install the dependencies:
  pip install -r requirements.txt

4.  
  Run migrations:

5.  Create a superuser:
  python manage.py createsuperuser

6.  Collect static files:
  python manage.py collectstatic

7.  Run the development server:
  python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/ to see the application.


## Usage

- Home Page: Displays featured article and a list of recent articles with pagination.
- Article Detail Page: Shows the full article, comments, and a form to add a new comment.
- Create Article: Authenticated users can create a new article.
- Edit/Delete Article: Authenticated users can edit or delete their own articles.
- Categories: View articles by category.
- Search: Search for articles by title.
- User Profile: View and manage your articles.

## Project Structure
- blog_app/: Contains the main user application with models, views, forms, and templates.
- core: Contains the core functionalities of the app.
- templates/: HTML templates for rendering views.
- static/: Static files like CSS and JavaScript.
- media/: Uploaded media files (like article thumbnails).
- requirements.txt: List of dependencies.

## Contributing
- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Make your changes.
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Create a new Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please contact:

Name: Jospeh Orokpo
GitHub: https://github.com/Josephorokpo
