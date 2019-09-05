import unittest
from conta_zeros import *

class TestContaZeros(unittest.TestCase):
    def test_conta_zeros_5(self):
        self.assertEqual(
            conta_zeros("00000"),
            5
        )

    def test_conta_zeros_0(self):
        self.assertEqual(
            conta_zeros("11111"),
            0
        )

    def test_conta_zeros_varios(self):
        self.assertEqual(
            conta_zeros("10101010010000100010010000000"),
            7
        )

    def test_conta_zeros_igual(self):
        self.assertEqual(
            conta_zeros("00100"),
            2
        )

    def test_conta_zeros_vazio(self):
        self.assertEqual(
            conta_zeros(''),
            0
        )

    def test_conta_zeros_int(self):
        self.assertRaises(
            TypeError,
            conta_zeros,
            100010
        )

    def test_conta_zeros_random(self):
        self.assertEqual(
            conta_zeros("hfxsyu\ndiugv7TER67TIGHVJG2YE2000YHJ GDKSULIDG2V0000YDSHJG DHKUC9YIV2GGL UIU"),
            4
        )

    def test_conta_zeros_so_zeros(self):
        self.assertEqual(
            conta_zeros("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000"),
            85
        )
    def test_conta_zeros_espacos(self):
        self.assertEqual(
            conta_zeros("00 000 0000"),
            4
        )
    
    def test_conta_zeros_um_espaco(self):
        self.assertEqual(
            conta_zeros(' '),
            0
        )
        

if __name__ == "__main__":
    unittest.main()