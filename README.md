# Home-Assignment

# Music API

## Overview

This project provides a REST API for managing songs, including functionalities to list all songs, retrieve details of a specific song by title, and rate a song.

## API Endpoints

### 1. List All Songs

- **Endpoint:** `GET /api/songs/`
- **Description:** Retrieve a paginated list of all songs.

### 2. Get Song Details by Title

- **Endpoint:** `GET /api/songs/`
- **Query Parameter:** `title` (string)
- **Description:** Retrieve all attributes of a song by its title.

### 3. Rate a Song

- **Endpoint:** `PUT /api/add-rating/<song_id>/`
- **Description:** Rate a song by its ID. The rating must be between 0 and 5.

## Setup and Running the Project

### Prerequisites

Ensure you have Python 3.6+ and pip installed.

### Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Create and Activate a Virtual Environment:**

    ```sh
    python -m venv venv
    ```

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create and Apply Migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Load Initial Data:**

    If you have a JSON file for initial data, make sure to add a script or command to load it. For example, if you have a `normalized_data_ops` script, you can do something like:

    ```python
    from normalized_data_ops import get_song_data, DataMigration

    data = get_song_data()
    DataMigration(data)
    ```

    Ensure this script is run in an appropriate way, such as through a management command or a custom script in your project.

6. **Run the Development Server:**

    ```sh
    python manage.py runserver
    ```

    You can now access the API at `http://localhost:8000/api/`.

## Running Tests

To ensure that everything is working correctly, you can run the unit tests:

```sh
python manage.py test


