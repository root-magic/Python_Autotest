from enum import Enum


class Routes(str, Enum):
    LOGIN = '/user/login/'
    REGISTRATION = '/user/registration/'
    SECURE_PAGE = '/user/profile/'
    CATALOG = '/catalog/vse-tovary'

    def __str__(self) -> str:
        return self.value