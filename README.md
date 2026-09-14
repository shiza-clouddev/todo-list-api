# To-Do List API

A simple, containerized To-Do List REST API built with Python and Flask.

## Endpoints

* **GET /**: Welcome message and documentation of available endpoints.
* **GET /todos**: Retrieve the list of all tasks.
* **POST /todos**: Add a new task. (Send JSON: `{"task": "Your task name"}`)
* **PUT /todos/<id>/done**: Mark a specific task as completed by its ID.

## How to Run Locally (Docker)

1. Build the Docker image:
   ```bash
   docker build -t todo-app .
