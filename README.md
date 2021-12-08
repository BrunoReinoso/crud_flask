# Crud Flask

## Description 
    A simple CRUD implementation with flask microframework.
    
## Architecture
  - A web application using Flask (python language).
  - A postgresql database.

## Development
This project was developed on Linux Ubuntu 21.04. 

Then, we recommend installing pyenv and pyenv-virtualenv, install python 3.8.0 on it and then create a pyenv virtualenv with this python version.

Alternatively, in case you need, there are also commands in the Makefile to build and run the containers for the app.

### Requisitions to api

  The requisitions were made with Postman but you can use other program if you want.


## Installation

### Clone the project

```bash
  git clone https://github.com/BrunoReinoso/crud_flask
```

### Activate the virtualenv and install the dependencies (if you want to use Docker, skip this step)

```bash
  make requirements-pip
```

### Up the container with database

```bash
  make docker-compose-up
```

### How to run app

```bash
    python app.py
```


# Author

- [@BrunoReinoso](https://github.com/BrunoReinoso/)