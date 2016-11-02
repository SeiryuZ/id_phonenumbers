__version__ = (0, 1, 6)

from id_phonenumbers.number import Number


def parse(phone_number):
    return Number(phone_number)
