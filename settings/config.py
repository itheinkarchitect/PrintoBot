from dotenv import load_dotenv
import os

load_dotenv()

print("TOKEN:", repr(os.getenv("BOT_TOKEN")))
print("OWNER_ID:", repr(os.getenv("OWNER_ID")))

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

if TOKEN is None:
    raise ValueError("BOT_TOKEN не найден в .env")

if OWNER_ID is None:
    raise ValueError("OWNER_ID не найден в .env")

OWNER_ID = int(OWNER_ID)