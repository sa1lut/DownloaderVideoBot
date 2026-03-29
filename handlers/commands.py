import re
import os

from aiogram import F, Router
from aiogram.types import FSInputFile, Message
from aiogram.filters import CommandStart, Command

from utils.downloadVideo import downloadVideo


router = Router()

@router.message(CommandStart())
async def startCommand(message: Message):
    await message.answer("Привет! Я бот для скачивания видео. Просто отправь мне ссылку на видео, и я его скачаю!")

@router.message(Command("help"))
async def helpCommand(message: Message):
    await message.answer("Это бот для скачивания видео. Просто отправь мне ссылку на видео, и я его скачаю!")

@router.message(F.text.contains("https://") | F.text.contains("http://"))
async def downloadCommand(message: Message):
    match = re.search(r"https?://\S+", message.text)

    if match:
        url = match.group()
    
        try:
            status_msg = await message.answer("Скачиваю видео...")
            file_path = await downloadVideo(url)

            await message.answer_video(video=FSInputFile(file_path))

            if message.chat.type == "group" or message.chat.type == "supergroup":
                await message.delete()  # Удаляем сообщение с ссылкой только в группах

            os.remove(file_path)

        except Exception as e:
                await message.answer(f"У меня произошла ошибка при скачивании видео с этой ссылкой. \nПожалуйста, попробуйте другую ссылку.")
            # Если файл всё же был создан, удаляем его
                if 'file_path' in locals() and os.path.exists(file_path):
                    os.remove(file_path)
        finally:
             await status_msg.delete()            

@router.message()
async def skipMessage(message: Message):
    pass 