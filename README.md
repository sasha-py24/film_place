# Films Place

A Django web application for film management and discovery.

## Installation

This project uses Poetry for dependency management. Make sure you have Poetry installed:

```bash
# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sasha-py24/film_place.git
cd film_place
```

2. Install dependencies:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Development

### Code Formatting

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **pre-commit** for git hooks

To format code:
```bash
poetry run black .
poetry run isort .
poetry run flake8 .
```

### Pre-commit Hooks

Install pre-commit hooks:
```bash
poetry run pre-commit install
```

## Project Structure

```
film_place/
├── films_place/          # Main Django project
├── movie/               # Movie app
├── core/                # Core app
├── user/                # User management app
├── templates/           # HTML templates
├── pyproject.toml      # Poetry configuration
└── README.md           # This file
```

## Security Considerations

- The project uses Django's built-in security features
- CSRF protection is enabled
- XSS protection is implemented
- Input validation is enforced
- Database queries are parameterized to prevent SQL injection

## Performance Optimizations

- Database queries are optimized
- Static files are properly configured
- Caching strategies can be implemented as needed
- Scalable architecture following Django best practices
