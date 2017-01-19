# 10 test cases for the prime numbers function

import unittest

from primenumbers import prime_numbers


class PrimeNumbersTestCase(unittest.TestCase):

#    def test_no_input(self):
#        self.assertIsNone(prime_numbers(None))

    def test_number_one(self):
        self.assertEqual('one is special', prime_numbers(1))

#    def test_string(self):
#        self.assertRaises(TypeError, prime_numbers('book'))

