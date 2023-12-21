# Insurance Backend

Welcome to insurance backend. This django based web application is used to create customers and process quotes and create policies for them. This is an assignment for democrance software engineer interview.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Policy creation** - Create policy for customers, filter them using `type`
- **Customer creation** - Create customers for the platform, search using `first_name` and `last_name`, and filter using `date_of_birth` (YYYY-MM-DD)

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Docker](https://www.docker.com/) installed
- [Docker Compose](https://docs.docker.com/compose/) installed

### Installation

1. Clone the repository:

    ```
    git clone git@github.com:divyanshudimri/insurance-backend.git
    ```

2. Navigate to the project directory:

    ```
    cd insurance-backend
    ```

3. Build and start the Docker containers:

    ```
    docker-compose up -d
    ```

### Local developement

Here is the way to install pre-commit hooks and poetry

1. Install poetry
    - Mac os, prerequisites `brew`
    ```
    brew install poetry
    ```
    - Ubuntu
    ```
    curl -sSL https://install.python-poetry.org
    POETRY_HOME=/usr/local/bin/poetry python3 -
    poetry config virtualenvs.create false
    ```

2. Activate virtual environment
    ```
    source $(poetry env info -p)/bin/activate
    ```

3. Install pre-commit hooks
    ```
    pre-commit install
    ```

### Configuration

The project uses environment variables for configuration. Edit the `.env` file and provide the necessary values, such as database connection details and API keys.

### Testing

- Go into backend container shell and run:

   ```
    python manage.py test
    ```


## Usage

Visit `http://0.0.0.0:65000` in your browser to access the Django application.

## API Documentation

Refer to the [API documentation](http://0.0.0.0:65000/docs/) for details on available endpoints and how to interact with the backend.
Alternate [API documentation](http://0.0.0.0:65000/redoc/)

## Notes
- `POST api/v1/customer/` expects date format to be in `YYYY-MM-DD`
- Link to documentation is a localhost link, build and start docker containers and then go to these links
