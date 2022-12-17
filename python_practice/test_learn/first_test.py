import unittest
from my_functions import f1
import requests

# python -m unittest first_test.MyTest


class MyTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(f1(10,5),15)

    def test_email(self):
        r = requests.get('https://initio-backend.onrender.com/email/409A-confirm')
        # print(r.status_code)
        # print(r.json())
        self.assertEqual(r.status_code, 300)




