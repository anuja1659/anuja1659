import json
import os

FILE = "todos.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=2)