### Description

This is a video streaming application similiar to Tiktok.

### Tech-stack for backend.

1. Django
2. PostgreSQL + MongoDB (currently SQLite for base development purpose)
3. Redis (for caching - popular videos)
4. RESTful API

### Local Setup

1. Clone this repository
2. Create virtual environment for this project.
3. Activate the virtual environment.
4. Store env variables for the project (neglect this). Install `direnv` (*nix system) and load the .envrc
5. `pip install -r requirements.txt` - install all dependencies.
6. `python manage.py migrate` - make database migrations and update tables.
7. `python manage.py runserver` - runs the backend server for application.
8. Fire up the browser and visit `127.0.0.1:8000/admin`

---
- ## <b>Add .env support to your django in development and deployments</b>
  - Setup envoirment
    1. Replicate first `.env.example` and rename to `.env` file
        <br/> Example: `tikup/.env`
        
    2. Config your `envoirment variable`.
    3. Done.

- ### Conclusion
    - The easiest and most common usage consists on calling `load_dotenv` when the application starts, which will load environment variables from a file named `.env` in the current directory or any of its parents or from the path specificied; after that, you can just call the environment-related method you need as provided by `os.getenv`.

    - `.env` looks like this:
    ```
    # a comment that will be ignored.
    REDIS_ADDRESS=localhost:6379
    MEANING_OF_LIFE=42
    MULTILINE_VAR="hello\nworld"
    ```

For more information about the `.env` click [here](https://pypi.org/project/python-dotenv/).

---