import unittest
from math_utils import es_par 

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4)) # 4 debería ser par

    def test_5_no_es_par(self):
        self.assertFalse(es_par(5)) # 5 debería ser impar

    def test_0_es_par(self):
        self.assertTrue(es_par(0))

    def test_negativos(self):
        # negativos funcionan igual
        self.assertTrue(es_par(-2))
        self.assertFalse(es_par(-3))

if __name__ == "__main__":
    unittest.main()