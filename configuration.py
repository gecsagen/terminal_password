import configparser
import os
from pathlib import Path
from generator import PasswordSettings
from exceptions import NotValidValueInConfig


def get_bool_from_string(string: str) -> bool:
    """Возвращает True или False из строки конфига"""
    if string.lower() == "true":
        return True
    elif string.lower() == "false":
        return False
    raise NotValidValueInConfig


def get_int_from_string(string: str) -> int:
    """Возвращает целое число из строки если это возможно"""
    try:
        result = int(string)
    except ValueError:
        raise NotValidValueInConfig
    return result


class Config:
    def get_config(self, path_config: str = "") -> PasswordSettings:
        # home_dir = os.path.expanduser("~")

        config = configparser.ConfigParser()
        config.read(f"settings.conf")

        # Получение значения настройки по ключу
        try:
            long = get_int_from_string(config.get("settings", "long"))
            quantity = get_int_from_string(config.get("settings", "quantity"))
            lowercase = get_bool_from_string(config.get("settings", "lowercase"))
            capital_letters = get_bool_from_string(
                config.get("settings", "capital_letters")
            )
            numbers = get_bool_from_string(config.get("settings", "numbers"))
            special_characters = get_bool_from_string(
                config.get("settings", "special_characters")
            )
            buffers = get_bool_from_string(config.get("settings", "buffer"))
        except ValueError:
            pass

        # return PasswordSettings(
        #     long=long,
        #     lowercase=lowercase,
        #     capital_letters=capital_letters,
        #     numbers=numbers,
        #     quantity=quantity,
        #     special_characters=special_characters,
        #     buffer=buffers,
        # )


g = Config()
# print(g.get_config())
print(get_bool_from_string("True"))
