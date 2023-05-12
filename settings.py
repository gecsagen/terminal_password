from argparse import ArgumentParser, BooleanOptionalAction, Namespace
from typing import Protocol

from collections import namedtuple

from exceptions import LongPasswordError
from generator import PasswordSettings

#  алиас для аргументов командной строки
ArgsRow = Namespace


def _get_args(parser: ArgumentParser) -> ArgsRow:
    """получает аргументы командной строки"""
    parser.add_argument(
        "--long", type=int, required=False, help="Длинна генерируемых паролей"
    )
    parser.add_argument(
        "--quantity", type=int, required=False, help="Количество генерируемых паролей"
    )

    aggregate = namedtuple("aggregate", "flag help default")

    templates = [
        ("--lowercase", "Использовать строчные буквы", True),
        ("--capital", "Использовать заглавные буквы", True),
        ("--numbers", "Использовать цифры", True),
        ("--special", "Использовать специальные символы", True),
        ("--buffer", "Копировать пароли в буффер обмена", False),
    ]
    for template in templates:
        args = aggregate(*template)
        parser.add_argument(
            args.flag,
            type=bool,
            required=False,
            help=args.help,
            default=args.default,
            action=BooleanOptionalAction,
        )
    results = parser.parse_args()
    return results


def validate_long(long: int | None) -> bool:
    """Валидирует значение длинны пароля, не меньше 6"""
    return True if long is None or long >= 6 else False


class SettingsStorage(Protocol):
    """протокол для реализации настроек генерации паролей"""

    @staticmethod
    def _get_settings() -> PasswordSettings:
        raise NotImplementedError


class SettingsPaswordStorage:
    @staticmethod
    def _get_settings() -> PasswordSettings:
        """возвращает настройки генерации паролей"""
        args_row = _get_args(ArgumentParser())
        settings = PasswordSettings()
        if validate_long(args_row.long):
            settings.long = args_row.long if args_row.long else settings.long
        else:
            raise LongPasswordError
        settings.quantity = (
            args_row.quantity if args_row.quantity else settings.quantity
        )
        settings.lowercase = (
            args_row.lowercase if not args_row.lowercase else settings.lowercase
        )
        settings.capital_letters = (
            args_row.capital if not args_row.capital else settings.capital_letters
        )
        settings.numbers = (
            args_row.numbers if not args_row.numbers else settings.numbers
        )
        settings.special_characters = (
            args_row.special if not args_row.special else settings.special_characters
        )
        settings.buffer = args_row.buffer if args_row.buffer else settings.buffer
        return settings


def get_set(storage: SettingsStorage) -> PasswordSettings:
    """возвращает настройки генерации паролей"""
    return storage._get_settings()
