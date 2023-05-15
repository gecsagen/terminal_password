import configparser
import os
import os.path
from pathlib import Path
from typing import Literal, Protocol

from exceptions import EmptyConfigError, NotValidValueInConfig
from settings import PasswordSettings


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


def file_exist(path: str) -> bool:
    if os.path.exists(path):
        return True
    return False


class ConfigStorage(Protocol):
    @staticmethod
    def _get_config(path_config: str = "") -> PasswordSettings:
        raise NotImplementedError


class Config:
    @staticmethod
    def _get_config(path_config: str = "settings.conf") -> PasswordSettings:
        """Возвращает настройки из конфига если они есть"""

        config = configparser.ConfigParser()

        if file_exist(path_config):
            config.read(path_config)
        else:
            raise EmptyConfigError

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
        except NotValidValueInConfig:
            raise EmptyConfigError

        return PasswordSettings(
            long=long,
            lowercase=lowercase,
            capital_letters=capital_letters,
            numbers=numbers,
            quantity=quantity,
            special_characters=special_characters,
            buffer=buffers,
        )


def get_config(storage: ConfigStorage, path_config: str = "") -> PasswordSettings:
    """возвращает настройки из конфига"""
    return storage._get_config(path_config)
