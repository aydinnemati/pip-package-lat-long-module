import unittest
from funcs import LatLong

class Test(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(LatLong(45, 45), {
            'country': 'Russia',
            'country_code': 'ru',
            'latitude': 45,
            'longitude': 45,
            'languages': ['ru'],
            'population': 146233000,
            'timezones': [
                'UTC+03:00',
                'UTC+04:00',
                'UTC+06:00',
                'UTC+07:00',
                'UTC+08:00',
                'UTC+09:00',
                'UTC+10:00',
                'UTC+11:00',
                'UTC+12:00'
                ]
            }
        )

    def testFalse(self):
        with self.assertRaises(ValueError):
            LatLong("aa", "ds")
if __name__ == '__main__':
    unittest.main()

    