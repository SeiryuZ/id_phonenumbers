import unittest

from indonesia_phone_parser.parser import Parser


class TestParser(unittest.TestCase):

    def test_get_area_code(self):
        parser = Parser('025221123456')
        parser.get_area_code()

        self.assertEqual(parser.area_code, '252')
        self.assertEqual(parser.area_name, 'Lebak')
        self.assertEqual(parser.regional_number, '21123456')

        parser = Parser('+62216628884')
        parser.get_area_code()

        self.assertEqual(parser.area_code, '21')
        self.assertEqual(parser.area_name, 'Jakarta, Tangerang')
        self.assertEqual(parser.regional_number, '6628884')

        parser = Parser('087782357971')
        parser.get_area_code()

        self.assertEqual(parser.area_code, None)
        self.assertEqual(parser.area_name, None)
        self.assertEqual(parser.regional_number, '87782357971')

    def test_parse(self):
        # Landline, should not be mobile
        parser = Parser('+62216628884')
        parser.parse()

        self.assertEqual(parser.carrier, None)
        self.assertEqual(parser.is_mobile, False)

        # CDMA, should be mobile
        parser = Parser('025221123456')
        parser.parse()

        self.assertEqual(parser.carrier, "Hepi (Mobile-8)")
        self.assertEqual(parser.is_mobile, True)
