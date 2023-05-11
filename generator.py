import random
import string
from dataclasses import dataclass
from typing import Protocol

#  константы с символами
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = "0123456789"
SPECIAL_CHAPTERS = "!@#$%^&*()_+№;%:?+"


@dataclass(slots=True)
class PasswordSettings:
    """Настройки генерации паролей"""

    long: int = 12
    quantity: int = 1
    lowercase: bool = True
    capital_letters: bool = True
    numbers: bool = True
    special_characters: bool = True
    buffer: bool = False


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

#  TODO: сделать гарантированное попадание в пароль хотябы 1 символа из каждого выбранного набора символов
class PasswordGenerStorage:
    def _generator_password(self, settings: PasswordSettings) -> Password:
        """Возвращает пароль"""
        final_characters = ""
        if settings.lowercase:
            final_characters += LOWERCASE
        if settings.capital_letters:
            final_characters += UPPERCASE
        if settings.numbers:
            final_characters += NUMBERS
        if settings.special_characters:
            final_characters += SPECIAL_CHAPTERS
        final_character_list = [character for character in final_characters]
        random.shuffle(final_character_list)
        password = "".join(final_character_list[: settings.long])
        return Password(text_password=password)

    def _generator_list_password(self, settings: PasswordSettings) -> list[Password]:
        """Возвращает список паролей"""
        list_password = [
            self._generator_password(settings) for x in range(settings.quantity)
        ]
        return list_password


def gener_password(
    settings: PasswordSettings, storage: PasswordStorage
) -> Password | list[Password]:
    """Генерирует пароль"""
    if settings.quantity == 1:
        return storage._generator_password(settings)
    else:
        return storage._generator_list_password(settings)

#  TODO: написать функцию копирования в буфер обмена сгенерированных паролей