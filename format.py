from typing import Protocol

import clipboard  # type: ignore

from generator import Password


class PinterStorage(Protocol):
    """Протокол печати паролей"""

    def _print_passwords(self, passwords: Password | list[Password]) -> None:
        raise NotImplementedError


class PinterPasswordStorage:
    """Реализация протокола печати"""

    def _print_passwords(self, passwords: Password | list[Password]) -> None:
        """Печатает список паролей"""
        if type(passwords) is list:
            for password in passwords:
                print(password.text_password)
        elif type(passwords) is Password:
            print(passwords.text_password)


def printer_passwords(
    passwords: Password | list[Password], storage: PinterStorage
) -> None:
    """Оболочка для вызова метода печати пароля"""
    storage._print_passwords(passwords)


def paste_in_buffer(password: Password | list[Password]) -> None:
    """Вставляет пароль в буфер обмена"""
    if type(password) is list:
        passwords = []
        for x in password:
            passwords.append(x.text_password)
        clipboard.copy("\n".join(passwords))
    elif type(password) is Password:
        clipboard.copy(password.text_password)


if __name__ == "__main__":
    paste_in_buffer(Password(text_password="Hello"))
