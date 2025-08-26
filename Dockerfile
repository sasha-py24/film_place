FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

COPY . .

CMD ["python", "manage.py", "runserver"]