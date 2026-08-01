from datetime import datetime
import json

from settings.paths import usersFile


def upsert_user(user_id: int, full_name: str):
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")

    if not usersFile.exists():
        users = []
    else:
        with open(usersFile, "r", encoding="utf-8") as f:
            users = json.load(f)

    for user in users:
        if user["user_id"] == user_id:
            user["full_name"] = full_name
            user["last_message_at"] = current_time

            with open(usersFile, "w", encoding="utf-8") as f:
                json.dump(users, f, ensure_ascii=False, indent=2)

            return

    users.append({
        "user_id": user_id,
        "full_name": full_name,
        "registered_at": current_time,
        "last_message_at": current_time
    })

    with open(usersFile, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def get_users():
    if not usersFile.exists():
        users = []
    else:
        with open(usersFile, "r", encoding="utf-8") as f:
            users = json.load(f)

    return users