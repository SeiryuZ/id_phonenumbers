import phonenumbers
# preload carrier
from phonenumbers import carrier as phonenumber_carrier  # noqa

from indonesia_phone_parser.area_code_metadata import AREA_CODE
from indonesia_phone_parser.carriers_metadata import CDMA_PREFIX_SPECIAL_AREA_CODE, CDMA_PREFIX


class Parser(object):

    def __init__(self, phone):
        self.phone = phone
        self.area_code = ''
        self.area_name = ''
        self.carrier = ''
        self.is_mobile = False

    def __unicode__(self):
        return "%s" % self.__dict__

    def parse(self):

        phone = phonenumbers.parse(self.phone, "ID")

        # 1st pass, try to find mobile carrier from phonenumbers
        self.carrier = phonenumbers.carrier.name_for_number(phone, "en")

        if self.carrier:
            self.is_mobile = True
            return
        else:
            national_number = str(phone.national_number)
            number_length = len(national_number)

            # 1. Try if area code is supplied with CDMA_PREFIX_SPECIAL_AREA_CODE
            carrier = CDMA_PREFIX_SPECIAL_AREA_CODE.get(national_number[:4])
            if carrier:
                self.is_mobile = True
                self.carrier = carrier
                return

            # 2. Check if it's length include area code or not
            # Without area code, must be 8
            # With area code, can be 10 or 11

            if number_length not in [8, 10, 11]:
                self.is_mobile = False
                return
            else:
                # assume without area code, check prefix directly
                if number_length == 8:
                    carrier = CDMA_PREFIX.get(national_number[:2]) or CDMA_PREFIX.get(national_number[:1])
                    area_code = ''
                    area_name = ''

                # Check if area_code is valid first
                elif number_length == 10:
                    area_code = national_number[:2]
                    area_name = AREA_CODE.get(area_code)
                    if area_name:
                        carrier = CDMA_PREFIX.get(national_number[2:3]) or CDMA_PREFIX.get(national_number[2:4])

                elif number_length == 11:
                    area_code = national_number[:3]
                    area_name = AREA_CODE.get(area_code)
                    if area_name:
                        carrier = CDMA_PREFIX.get(national_number[3:4]) or CDMA_PREFIX.get(national_number[3:5])

                if carrier:
                    self.is_mobile = True
                    self.carrier = carrier
                    self.area_code = area_code
                    self.area_name = area_name
