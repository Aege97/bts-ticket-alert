import json
import os

STATE_FILE = "state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"available": False}

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(available):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"available": available}, f)