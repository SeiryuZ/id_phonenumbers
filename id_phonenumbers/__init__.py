__version__ = (0, 1, 1)

from id_phonenumbers.number import Number


def parse(phone_number):
    return Number(phone_number)
