import asyncio

from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from settings.users_storage import upsert_user, get_users
from settings.config import OWNER_ID

from services.formatter import format_message, format_users
from services.printer import print_text

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    user_id = user.id
    full_name = user.full_name

    upsert_user(user_id, full_name)

    await message.answer("Привет! Этот бот поможет напечатать текст в ирл")

@router.message(Command("users"))
async def cmd_users(message: Message):
    user = message.from_user

    if user.id != OWNER_ID:
        await message.answer("У вас нет доступа")
        return

    users = get_users()

    text = format_users(users)

    await message.answer(text)

@router.message()
async def forward_message(message: Message, bot: Bot):
    user = message.from_user

    upsert_user(user.id, user.full_name)

    formatted_text = format_message(full_name=user.full_name, user_id=user.id, text=message.text)

    await bot.send_message(chat_id=OWNER_ID, text=formatted_text)

    if print_text(message.text):
        await message.answer("✅ Сообщение отправлено на печать.")
    else:
        await message.answer("❌ Ошибка печати.")