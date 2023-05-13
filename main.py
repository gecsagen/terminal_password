from exceptions import LongPasswordError
from format import (
    PinterPasswordStorage,
    paste_in_buffer,
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

    #  печать паролей в консоль
    printer_passwords(password, PinterPasswordStorage())

    #  вставка паролей в буфер, если требуется
    if settings.buffer:
        paste_in_buffer(password)


if __name__ == "__main__":
    main()
