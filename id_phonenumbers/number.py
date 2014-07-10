import phonenumbers

from id_phonenumbers.area_code_metadata import AREA_CODE
from id_phonenumbers.carriers_metadata import CDMA_PREFIX, GSM_PREFIX


class Number(object):

    def __init__(self, phone):
        self.phone = phone
        self._phone = phonenumbers.parse(self.phone, "ID")

        self.national_number = str(self._phone.national_number)
        self.local_number = None

        self.carrier = None
        self.area_code = None
        self.area_name = None
        self.is_mobile = False

        self.parse()

    def __unicode__(self):
        return "%s" % self.__dict__

    def parse_area_code(self):
        if self.phone:
            # Test for 3-number area code
            self.area_name = AREA_CODE.get(self.national_number[:3])
            if self.area_name is not None:
                self.area_code = self.national_number[:3]
                self.local_number = self.national_number[3:]

            # Test for 2-number area code
            else:
                self.area_name = AREA_CODE.get(self.national_number[:2])
                if self.area_name:
                    self.area_code = self.national_number[:2]
                    self.local_number = self.national_number[2:]

            # If cannot determine Area Name,  assume given number is local number
            if self.area_name is None:
                self.local_number = self.national_number

        return None

    def parse(self):
        self.parse_area_code()

        number_length = len(self.local_number)

        # GSM prefix always have 10 to 12 number length.
        if number_length in (9, 10, 11):
            self.carrier = GSM_PREFIX.get(self.local_number[:3])

        # Try to check CDMA prefix, always have 8 number length
        if number_length == 8:
            self.carrier = CDMA_PREFIX.get(self.local_number[:2]) \
                or CDMA_PREFIX.get(self.local_number[:1])

        if self.carrier:
            self.is_mobile = True
