from typing import Protocol

import clipboard  # type: ignore

from generator import Password


class PinterStorage(Protocol):
    """Протокол печати паролей"""

    def _print_passwords(self, passwords: list[Password]) -> None:
        raise NotImplementedError

    def _print_password(self, passwords: Password) -> None:
        raise NotImplementedError


class PinterPasswordStorage:
    """Реализация протокола печати"""

    def _print_passwords(self, passwords: list[Password]) -> None:
        """Печатает список паролей"""
        for password in passwords:
            print(password.text_password)

    def _print_password(self, passwords: Password) -> None:
        """Печатает 1 пароль"""
        print(passwords.text_password)


def printer_password(password: Password, storage: PinterStorage) -> None:
    """Оболочка для вызова метода печати пароля"""
    storage._print_password(password)


def printer_passwords(passwords: list[Password], storage: PinterStorage) -> None:
    """Оболочка для вызова метода печати пароля"""
    storage._print_passwords(passwords)


def paste_in_buffer(text: Password | list[Password]) -> None:
    """Вставляет текст в буфер обмена"""
    if type(text) is list:
        paste_in_buffer_list(text)
    elif type(text) is Password:
        clipboard.copy(text.text_password)


def paste_in_buffer_list(passwords_list: list[Password]):
    passwords = []
    for x in passwords_list:
        passwords.append(x.text_password)
    clipboard.copy("\n".join(passwords))


if __name__ == "__main__":
    paste_in_buffer(Password(text_password="Hello"))
