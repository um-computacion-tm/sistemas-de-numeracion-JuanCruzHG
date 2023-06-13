import unittest
from decimal2 import decimal2binario, decimal2hexadecimal, decimal2octal
from binario import binario2decimal, binario2hexadecimal, binario2octal
from octal import octal2binario, octal2decimal, octal2hexadecimal
from hexadecimal import hexadecimal2binario, hexadecimal2decimal, hexadecimal2octal


class TestNumeracion(unittest.TestCase):
    def test_binario2decimal_1(self):
        self.assertEqual(binario2decimal('01011100'), 92)

    def test_binario2decimal_2(self):
        self.assertEqual(binario2decimal('1100001'), 97)

    def test_binario2hexadecimal(self):
        self.assertEqual(binario2hexadecimal('10100100'), "A4")

    def test_binario2octal(self):
        self.assertEqual(binario2octal('1100001'), 141)

    def test_decimal2binario_1(self):
        self.assertEqual(decimal2binario(97), '1100001')

    def test_decimal2binario_2(self):
        self.assertEqual(decimal2binario(92), '1011100')

    def test_decimal2hexadecimal(self):
        self.assertEqual(decimal2hexadecimal(105), '69')

    def test_decimal2octal(self):
        self.assertEqual(decimal2octal(123), 173)

    def test_hexadecimal2binario(self):
        self.assertEqual(hexadecimal2binario("F5"), "11110101")

    def test_hexadecimal2decimal(self):
        self.assertEqual(hexadecimal2decimal("C"), 12)

    def test_hexadecimal2octal(self):
        self.assertEqual(hexadecimal2octal("FA23"), 175043)
    
    def test_octal2binario(self):
        self.assertEqual(octal2binario(5), "101")

    def test_octal2decimal(self):
        self.assertEqual(octal2decimal(55), 45)

    def test_octal2hexadecimal(self):
        self.assertEqual(octal2hexadecimal(72), "3A")



if __name__ == '__main__':
    unittest.main()