# PROJECT

**Disclaimer:** This project is only to be used as a reference, for example for the logic used. So adjust its use according to your own needs.

## How to

- Start XAMPP
- Go to PHPMyAdmin Query, and write

```sql
CREATE DATABASE short_term_db;
CREATE DATABASE long_term_db;
```

- Open project root terminal and type

```sh
pip install -r requirements.txt
python manage.py makemigrations presence
python manage.py migrate --database=default
python manage.py migrate --database=long_term
uvicorn src.asgi:application --reload
```

For migration, Django requires MariaDB 10.5 or later, so upgrading MariaDB is recommended.
