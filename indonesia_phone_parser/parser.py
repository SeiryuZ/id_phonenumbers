import phonenumbers
from phonenumbers import carrier


AREA_CODE = {

    "21": "Jakarta, Tangerang",
    "252": "Lebak",
    "253": "Pandeglang",
    "254": "Cilegon, Serang",

    "22": True,
    "231": True,
    "232": True,
    "233": True,
    "234": True,
    "251": True,
    "260": True,
    "261": True,
    "262": True,
    "263": True,
    "264": True,
    "265": True,
    "266": True,
    "267": True,

    '24': True,
    '271': True,
    '272': True,
    '273': True,
    '274': True,
    '275': True,
    '276': True,
    '280': True,
    '281': True,
    '282': True,
    '283': True,
    '284': True,
    '285': True,
    '286': True,
    '287': True,
    '288': True,
    '289': True,

    '291': True,
    '292': True,
    '293': True,
    '294': True,
    '295': True,
    '296': True,
    '297': True,
    '298': True,
}

CDMA_PREFIX_WITH_AREA_CODE = {

    "9": "Esia",  # (Area-Code) - 9xxx-xxxx
    "83": "Esia",  # 021-83xx-xxxx

    "54": "TelkomFlexi",  # (area-code)-54xx-xxxx
    "70": "TelkomFlexi",  # (area-code)-70xx-xxxx
    "80": "TelkomFlexi",  # (area-code)-80xx-xxxx
    "81": "TelkomFlexi",  # (area-code)-81xx-xxxx
    "68": "TelkomFlexi",  # (area-code)-68xx-xxxx
    "3": "TelkomFlexi",  # (area-code)-3xxx-xxxx

    "61": "Indosat",  # (Area-code)-61xx-xxxx
    "62": "Indosat",  # (Area-code)-62xx-xxxx
    "63": "Indosat",  # (Area-code)-63xx-xxxx
    "90": "Indosat",  # (Area-code)-90xx-xxxx
    "30": "Indosat",  # 021-30xx-xxxx
    "60": "Indosat",  # 021-60xx-xxxx

    "50": "Hepi (Mobile-8)",  # (Area-code)-50xx-xxxx
    "21": "Hepi (Mobile-8)",  # (Area-code)-21xx-xxxx
    "31": "Hepi (Mobile-8)",  # (Area-code)-31xx-xxxx

}

CDMA_PREFIX_SPECIAL_AREA_CODE = {
    "2180": "Esia",  # 021 - 80xx-xxxx
    "2183": "Esia",  # 021 - 83xx-xxxx,

    "2170": "TelkomFlexi",  # 021-70xx-xxxx
    "2168": "TelkomFlexi",  # 021-68xx-xxxx

    "2130": "Indosat",  # 021-30xx-xxxx
    "3160": "Indosat",  # 031-60xx-xxxx
}


class Parser(object):

    phone = ''

    province_name = ''
    area_code = ''
    area_name = ''

    mobile_provider = ''

    is_mobile = False

    def __init__(self, phone):
        self.phone = phone

    def parse(self):

        phone = phonenumbers.parse(self.phone, "ID")
        # 1st pass, try to find mobile carrier from phonenumbers

        self.mobile_provider = carrier.name_for_number(phone, "en")

        if self.mobile_provider:
            self.is_mobile = True
        else:
            national_number = phone.national_number

            # 1. Try if area code is supplied with CDMA_PREFIX_SPECIAL_AREA_CODE
            if CDMA_PREFIX_SPECIAL_AREA_CODE.get(str(national_number[:4]), False):
                self.is_mobile = True
                return

            # 2. Try CDMA_PREFIX_WITH_AREA_CODE, assume phone with area code
