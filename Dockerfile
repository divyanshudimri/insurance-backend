# Use a Python base image
FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk update && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev linux-headers python3-dev && \
    apk add bash coreutils curl postgresql-client postgresql-libs

RUN mkdir -p /code/

# Set the working directory in the container
WORKDIR /code

# Copy the poetry.lock and pyproject.toml files
COPY pyproject.toml poetry.lock /code/

ENV PATH "/usr/local/bin/poetry/bin:${PATH}"

# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local/bin/poetry python3 - \
    && poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

# Copy the project code to the container
COPY . /code/

# Expose the Django development server port
EXPOSE 8000

CMD ["bash", "-i"]
