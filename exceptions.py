class LongPasswordError(Exception):
    """Длинна пароля меньше 6 символов"""


class NotValidValueInConfig(Exception):
    """Не валидное значение в файле конфига"""


class EmptyConfigError(Exception):
    """Конфиг отсутствует"""
