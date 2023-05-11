from format import PinterPasswordStorage, printer_password, printer_passwords
from generator import Password, PasswordGenerStorage, gener_password
from settings import SettingsPaswordStorage, get_set


def main() -> None:
    #  получение настроек для генерации паролей
    settings = get_set(SettingsPaswordStorage)
    #  получение сгенерированных паролей
    password = gener_password(settings, PasswordGenerStorage())
    #  печать паролей в консоль
    if type(password) is list:
        printer_passwords(password, PinterPasswordStorage())
    if type(password) is Password:
        printer_password(password, PinterPasswordStorage())


if __name__ == "__main__":
    main()