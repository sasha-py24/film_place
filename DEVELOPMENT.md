# Development Guide

## Poetry Setup

This project uses Poetry for dependency management. Here's how to get started:

### Prerequisites

1. **Install Poetry** (if not already installed):
   ```bash
   # Windows
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

   # macOS/Linux
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install Python 3.8.1+** (required for this project)

### Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sasha-py24/film_place.git
   cd film_place
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

4. **Navigate to Django project**:
   ```bash
   cd films_place
   ```

5. **Run database migrations**:
   ```bash
   poetry run python manage.py migrate
   ```

6. **Create superuser** (optional):
   ```bash
   poetry run python manage.py createsuperuser
   ```

7. **Start development server**:
   ```bash
   poetry run python manage.py runserver
   ```

### Development Workflow

#### Adding Dependencies

**Production dependencies**:
```bash
poetry add package-name
```

**Development dependencies**:
```bash
poetry add --group dev package-name
```

#### Code Quality Tools

This project includes several code quality tools:

- **Black** (code formatting): `poetry run black .`
- **isort** (import sorting): `poetry run isort .`
- **flake8** (linting): `poetry run flake8 .`

**Run all formatting**:
```bash
poetry run black . && poetry run isort . && poetry run flake8 .
```

#### Pre-commit Hooks

Install pre-commit hooks to automatically format code on commit:

```bash
poetry run pre-commit install
```

#### Running Tests

```bash
poetry run python manage.py test
```

#### Database Operations

```bash
# Create migrations
poetry run python manage.py makemigrations

# Apply migrations
poetry run python manage.py migrate

# Reset database (careful!)
poetry run python manage.py flush
```

### Project Structure

```
film_place/
├── films_place/          # Django project root
│   ├── manage.py        # Django management script
│   ├── films_place/     # Main Django project
│   ├── movie/           # Movie app
│   ├── core/            # Core app
│   ├── user/            # User management app
│   └── templates/       # HTML templates
├── pyproject.toml       # Poetry configuration
├── poetry.lock          # Locked dependencies
└── README.md           # Project documentation
```

### Security Best Practices

1. **Environment Variables**: Never commit sensitive data to version control
2. **Dependencies**: Keep dependencies updated and audit regularly
3. **Database**: Use parameterized queries to prevent SQL injection
4. **Authentication**: Use Django's built-in authentication system
5. **CSRF Protection**: Always include CSRF tokens in forms

### Performance Considerations

1. **Database Queries**: Use `select_related()` and `prefetch_related()` for related objects
2. **Caching**: Implement caching for frequently accessed data
3. **Static Files**: Use Django's static file handling
4. **Database Indexing**: Add indexes for frequently queried fields

### Troubleshooting

#### Poetry Issues

**If Poetry commands fail**:
```bash
# Clear Poetry cache
poetry cache clear --all pypi

# Reinstall dependencies
poetry install --sync
```

**If virtual environment issues occur**:
```bash
# Remove and recreate virtual environment
poetry env remove python
poetry install
```

#### Django Issues

**If migrations fail**:
```bash
# Reset migrations (careful - this will lose data!)
poetry run python manage.py migrate --fake-initial
```

**If static files don't load**:
```bash
# Collect static files
poetry run python manage.py collectstatic
```

### Deployment

For production deployment:

1. Set `DEBUG = False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving (nginx/Apache)
4. Use environment variables for sensitive settings
5. Configure proper logging
6. Set up monitoring and error tracking

### Contributing

1. Create a feature branch
2. Make your changes
3. Run code quality tools: `poetry run black . && poetry run isort . && poetry run flake8 .`
4. Run tests: `poetry run python manage.py test`
5. Submit a pull request
