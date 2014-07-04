import phonenumbers

from id_phonenumbers.area_code_metadata import AREA_CODE
from id_phonenumbers.carriers_metadata import CDMA_PREFIX


class Number(object):

    def __init__(self, phone):
        self.phone = phone
        self._phone = phonenumbers.parse(self.phone, "ID")

        self.national_number = str(self._phone.national_number)
        self.regional_number = None

        self.carrier = None
        self.area_code = None
        self.area_name = None
        self.is_mobile = False

    def __unicode__(self):
        return "%s" % self.__dict__

    def get_area_code(self):
        if self.phone:
            # Test for 3-number area code
            self.area_name = AREA_CODE.get(self.national_number[:3])
            if self.area_name is not None:
                self.area_code = self.national_number[:3]
                self.regional_number = self.national_number[3:]

            # Test for 2-number area code
            else:
                self.area_name = AREA_CODE.get(self.national_number[:2])
                if self.area_name:
                    self.area_code = self.national_number[:2]
                    self.regional_number = self.national_number[2:]

            # If cannot determine Area Name,  assume given number is regional number
            if self.area_name is None:
                self.regional_number = self.national_number

        return None

    def parse(self):
        self.get_area_code()

        # TODO: Check Mobile Carrier Prefix

        # Try to check CDMA prefix
        if len(self.regional_number) == 8:
            self.carrier = CDMA_PREFIX.get(self.regional_number[:2]) or CDMA_PREFIX.get(self.regional_number[:1])

            if self.carrier:
                self.is_mobile = True
