# 10 test cases for the prime numbers function

import unittest


class PrimeNumbersTestCase(unittest.TestCase):

    def test_no_input(self):
        self.assertIsNone(prime_numbers(None))

    def test_small_integer(self):
        self.assertIsInstance(4, prime_numbers(10))

    def test_large_integer(self):
        self.assertIsInstance(2999, prime_numbers(4000))

    def test_number_one(self):
        self.assertEqual('one is special', prime_number(1))

    def test_string(self):
        self.assertRaises(TypeError, prime_numbers('book'))

