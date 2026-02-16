import unittest
from math_utils import es_multiplo_de

class TestEsMultiploDe(unittest.TestCase):
    def test_4_es_multiplo_de_2(self):
        self.assertTrue(es_multiplo_de(4,2))
    def test_5_no_es_multiplo_de_2(self):
        self.assertFalse(es_multiplo_de(5,2))
    def test_0_es_multiplo_de_5(self):
        self.assertTrue(es_multiplo_de(0,5))
    def test_menos_5_no_es_multiplo_de_2(self):
        self.assertFalse(es_multiplo_de(-5,2))

if __name__ == "__main__":
    unittest.main()