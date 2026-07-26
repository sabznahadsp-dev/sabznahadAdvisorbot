import json
import os

DATA_FILE = "data/users.json"


def load_users():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except:
            return {}


def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


def user_exists(user_id):
    users = load_users()
    return str(user_id) in users


def get_user(user_id):
    users = load_users()
    return users.get(str(user_id))


def save_user(user_id, data):
    users = load_users()
    users[str(user_id)] = data
    save_users(users)