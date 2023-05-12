from exceptions import LongPasswordError
from format import (
    PinterPasswordStorage,
    paste_in_buffer,
    printer_password,
    printer_passwords,
)
from generator import Password, PasswordGenerStorage, PasswordSettings, gener_password
from settings import SettingsPaswordStorage, get_set


def main() -> None:
    #  получение настроек для генерации паролей
    try:
        settings: PasswordSettings = get_set(SettingsPaswordStorage)
    except LongPasswordError:
        print("Пароль должен быть длинее 6 символов в целях безопасности!")
        exit(1)
    #  получение сгенерированных паролей
    password = gener_password(settings, PasswordGenerStorage())
    #  печать паролей в консоль и копирование в буфер
    if type(password) is list:
        printer_passwords(password, PinterPasswordStorage())
        passwords = []
        if settings.buffer:
            for x in password:
                passwords.append(x.text_password)
        paste_in_buffer("\n".join(passwords))
    if type(password) is Password:
        printer_password(password, PinterPasswordStorage())
        if settings.buffer:
            paste_in_buffer(password.text_password)


if __name__ == "__main__":
    main()
