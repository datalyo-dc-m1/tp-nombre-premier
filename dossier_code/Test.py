import unittest


class NumberTest(unittest.TestCase):
        def test_get_color(self):
            self.assertEqual("La voiture est de color rouge", Car("rouge").get_color())

        def test_compare_color(self):
            self.assertEqual(False, Car("rouge").compare_color("bleu"))