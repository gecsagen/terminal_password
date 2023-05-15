import random
import string
from dataclasses import dataclass
from typing import Protocol

from settings import PasswordSettings

#  константы с символами
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = "0123456789"
SPECIAL_CHAPTERS = "!@#$%^&*()_+№;%:?+"


@dataclass(slots=True)
class Password:
    """Пароль"""

    text_password: str


class PasswordStorage(Protocol):
    """Интерфейс для генерации пароля"""

    def _generator_password(self, settings: PasswordSettings) -> Password:
        raise NotImplementedError

    def _generator_list_password(self, settings: PasswordSettings) -> list[Password]:
        raise NotImplementedError


class PasswordGenerStorage:
    def _generator_password(self, settings: PasswordSettings) -> Password:
        """Возвращает пароль"""
        suits = []
        if settings.lowercase:
            suits.append(LOWERCASE)
        if settings.capital_letters:
            suits.append(UPPERCASE)
        if settings.numbers:
            suits.append(NUMBERS)
        if settings.special_characters:
            suits.append(SPECIAL_CHAPTERS)
        final_character_list = [character for character in "".join(suits)]
        while True:
            random.shuffle(final_character_list)
            password = "".join(final_character_list[: settings.long])
            if check_password(suits, password):
                return Password(text_password=password)

    def _generator_list_password(self, settings: PasswordSettings) -> list[Password]:
        """Возвращает список паролей"""
        list_password = [
            self._generator_password(settings) for x in range(settings.quantity)
        ]
        return list_password


def check_password(suits: list[str], password: str) -> bool:
    """
    Проверяет содержит ли пароль хоть
    1 символ из переданных наборов символов
    """
    results_list = [any(char in suit for char in password) for suit in suits]
    return all(results_list)


def gener_password(
    settings: PasswordSettings, storage: PasswordStorage
) -> Password | list[Password]:
    """Генерирует пароль"""
    if settings.quantity == 1:
        return storage._generator_password(settings)
    return storage._generator_list_password(settings)
