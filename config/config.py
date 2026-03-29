import os
from dataclasses import dataclass


@dataclass
class Config:
    bot_token: str


def get_config() -> Config:
    # Здесь можно добавить логику для загрузки конфигурации из файла, переменных окружения и т.д.
    return Config(
        bot_token=os.getenv("BOT_TOKEN")
    )

settings = get_config()