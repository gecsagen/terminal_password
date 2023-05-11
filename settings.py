from argparse import ArgumentParser, BooleanOptionalAction, Namespace
from typing import Protocol

from generator import PasswordSettings

#  алиас для аргументов командной строки
ArgsRow = Namespace

#  TODO добавить ограничение на поле long, чтобы оно не могло быть меньше 6 символов, реализовать в виде функции
#  TODO создать кастомное исключение для этого случая
def _get_args(parser: ArgumentParser) -> ArgsRow:
    """получает аргументы командной строки"""
    parser.add_argument(
        "--long", type=int, required=False, help="Длинна генерируемых паролей"
    )
    parser.add_argument(
        "--quantity", type=int, required=False, help="Количество генерируемых паролей"
    )
    parser.add_argument(
        "--lowercase",
        type=bool,
        required=False,
        help="Использовать строчные буквы",
        default=True,
        action=BooleanOptionalAction,
    )
    parser.add_argument(
        "--capital",
        type=bool,
        required=False,
        help="Использовать заглавные буквы",
        default=True,
        action=BooleanOptionalAction,
    )
    parser.add_argument(
        "--numbers",
        type=bool,
        required=False,
        help="Использовать цифры",
        default=True,
        action=BooleanOptionalAction,
    )
    parser.add_argument(
        "--special",
        type=bool,
        required=False,
        help="Использовать специальные символы",
        default=True,
        action=BooleanOptionalAction,
    )
    parser.add_argument(
        "--buffer",
        type=bool,
        required=False,
        help="Копировать пароли в буффер обмена",
        default=False,
        action=BooleanOptionalAction,
    )

    args = parser.parse_args()
    return args


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
        settings.long = args_row.long if args_row.long else settings.long
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
        settings.buffer = args_row.buffer if not args_row.buffer else settings.buffer
        return settings


def get_set(storage: SettingsStorage) -> PasswordSettings:
    """возвращает настройки генерации паролей"""
    return storage._get_settings()
