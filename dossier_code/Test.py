from dossier_code.modelisation import Number
import unittest


class NumberTest(unittest.TestCase):
        def test_is_divisible(self):
            self.assertEqual(False, Number(5).is_divisible())

        def test_isprime(self):
            self.assertEqual(True, Number(14).is_prime())