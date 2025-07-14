import unittest
from src.email_validation.util import filter_mail

class TestEmailValidation(unittest.TestCase):

    def test_email(self):
        emails = [
            'lara@hackerrank.com',
            'brian-23@hackerrank.com',
            'britts_54@hackerrank.com'
        ]
        expected = sorted(emails)
        self.assertEqual(filter_mail(emails), expected)

    def test_email_negative_validation(self):
        emails = [
            'lara@hackerrank.com',
            'brian-23@hackerrank.com',
            'britts_54@hackerrank.com',
            'name@server.or',
            'name@site.c'
        ]
        expected = sorted([
            'lara@hackerrank.com',
            'brian-23@hackerrank.com',
            'britts_54@hackerrank.com'
        ])
        self.assertEqual(filter_mail(emails), expected)
