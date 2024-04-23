FROM python:3.9.19-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -y pipx libpq-dev gcc python3-dev postgresql && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pipx install poetry

WORKDIR /app

COPY ./people.py people_init.py sql.py poetry.lock pyproject.toml ./
COPY .venv .venv

ENV PATH="/app/.venv/bin:${PATH}:/root/.local/bin"

RUN poetry install

# SHELL [ "poetry", "shell" ]
CMD [ "bash" ]
