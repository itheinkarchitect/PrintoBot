from datetime import datetime

def format_message(full_name, user_id, text):

    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")

    formatted_text = f"""
    📥 Новая заявка

    👤 Пользователь: {full_name}
    🆔 ID: {user_id}
    🕒 Время: {current_time}

    ────────────────────────

    {text}
    """

    return formatted_text

def format_users(users: list) -> str:
    if not users:
        return "📂 База пользователей пуста."

    text = f"👥 Пользователи ({len(users)})\n\n"

    for number, user in enumerate(users, start=1):
        text += (
            f"#{number}\n"
            f"👤 {user['full_name']}\n"
            f"🆔 {user['user_id']}\n"
            f"📅 Регистрация: {user['registered_at']}\n"
            f"🕒 Последнее сообщение: {user['last_message_at']}\n"
            "────────────────────────\n"
        )

    return text