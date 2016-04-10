import unittest

from id_phonenumbers.number import Number


class TestNumber(unittest.TestCase):

    def test_parse_area_code(self):
        parser = Number('025221123456')
        parser.parse_area_code()

        self.assertEqual(parser.area_code, '252')
        self.assertEqual(parser.area_name, 'Lebak')
        self.assertEqual(parser.local_number, '21123456')

        parser = Number('+62216628884')
        parser.parse_area_code()

        self.assertEqual(parser.area_code, '21')
        self.assertEqual(parser.area_name, 'Jakarta, Tangerang')
        self.assertEqual(parser.local_number, '6628884')

        parser = Number('087782357971')
        parser.parse_area_code()

        self.assertEqual(parser.area_code, None)
        self.assertEqual(parser.area_name, None)
        self.assertEqual(parser.local_number, '87782357971')

    def test_parse(self):
        # Landline, should not be mobile
        parser = Number('+62216628884')
        parser.parse()

        self.assertEqual(parser.carrier, None)
        self.assertEqual(parser.is_mobile, False)

        # CDMA, should be mobile
        parser = Number('025221123456')
        parser.parse()

        self.assertEqual(parser.carrier, "Hepi (Mobile-8)")
        self.assertEqual(parser.is_mobile, True)

        # GSM, should be mobile
        parser = Number('087782357971')
        parser.parse()

        self.assertEqual(parser.carrier, "XL")
        self.assertEqual(parser.is_mobile, True)

        # Mobile CDMA
        parser = Number('088819001234')
        parser.parse()

        self.assertEqual(parser.carrier, "Smartfren")
        self.assertEqual(parser.is_mobile, True)

        parser = Number('08886175555')
        parser.parse()

        self.assertEqual(parser.carrier, "Smartfren")
        self.assertEqual(parser.is_mobile, True)
