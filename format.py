from typing import Protocol

from generator import Password


class PinterStorage(Protocol):
    """Протокол печати паролей"""
    def _print_passwords(self, passwords: list[Password]):
        raise NotImplementedError

    def _print_password(self, passwords: Password) -> None:
        raise NotImplementedError


class PinterPasswordStorage:
    """Реализация протокола печати"""
    def _print_passwords(self, passwords: list[Password]):
        """Печатает список паролей"""
        for password in passwords:
            print(password.text_password)

    def _print_password(self, passwords: Password) -> None:
        """Печатает 1 пароль"""
        if type(passwords) is Password:
            print(passwords.text_password)


def printer_password(password: Password, storage: PinterStorage):
    """Оболочка для вызова метода печати пароля"""
    storage._print_password(password)


def printer_passwords(passwords: list[Password], storage: PinterStorage):
    """Оболочка для вызова метода печати пароля"""
    storage._print_passwords(passwords)
