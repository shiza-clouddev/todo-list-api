from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []


@app.route("/", methods=["GET"])
def home():
  return jsonify(
      {
          "message": "Welcome to To-Do API",
          "endpoints": {
              "GET /todos": "View all tasks",
              "POST /todos": "Add a new task",
              "PUT /todos/<id>/done": "Mark task as done",
          },
      }
  )


@app.route("/todos", methods=["GET"])
def get_todos():
  return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
  data = request.get_json()
  new_task = {
      "id": len(todos) + 1,
      "task": data.get("task"),
      "done": False,
  }
  todos.append(new_task)
  return jsonify(new_task), 201


@app.route("/todos/<int:todo_id>/done", methods=["PUT"])
def mark_done(todo_id):
  for todo in todos:
    if todo["id"] == todo_id:
      todo["done"] = True
      return jsonify(todo)
  return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
