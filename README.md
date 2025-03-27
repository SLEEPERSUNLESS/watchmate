# Watchmate

Watchmate is a Django-based web application designed to manage and track your movie and TV show watchlists. It provides a simple yet powerful way to keep track of what you have watched and what you plan to watch.

## Features

- **User Authentication**: Secure user registration and login functionality.
- **Watchlist Management**: Add, update, and remove movies or TV shows from your personal watchlist.
- **Status Tracking**: Mark items as 'Watched' or 'Unwatched' to keep track of your viewing progress.
- **API Support**: Fully functional REST API that allows integration with external applications.

## Project Structure

- `watchmate/`: Main project directory containing settings and configuration files.
- `user_app/`: Handles user authentication and profile management.
- `watchlist_app/`: Manages the core functionality related to watchlist operations.
- `db.sqlite3`: SQLite database file storing application data.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: Lists the Python dependencies required to run the project.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SLEEPERSUNLESS/watchmate.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd watchmate
   ```

3. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (for accessing the Django admin interface):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the superuser account.

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## API Testing

For best results, it is recommended to use **Postman** to test the API endpoints effectively. Postman provides an intuitive interface for making API requests and viewing responses in an organized manner.

## Usage

- **Register/Login**: Create a new account or log in with existing credentials.
- **Manage Watchlist**: Add new movies or TV shows, update their status, and remove them as needed.
- **Admin Interface**: Access Django's admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
