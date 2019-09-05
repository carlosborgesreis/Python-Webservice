import unittest
from services.converte_romano import *

class TestConverteRomano(unittest.TestCase):
  def test_valida_numero_true(self):
    self.assertTrue(
      valida_numero(3999)
    )

  def test_valida_numero_false(self):
    self.assertFalse(
      valida_numero(4000)
    )

  def test_valida_numero_string(self):
    self.assertTrue(
      valida_numero("3999")
    )

  def test_valida_numero_zero(self):
    self.assertFalse(
      valida_numero(0)
    )

  def test_valida_numero_negativo(self):
    self.assertFalse(
      valida_numero(-20)
    )

  def test_numero_para_romano_true(self):
    self.assertEqual(
      numero_para_romano(9),
      "IX"
    )

  def test_numero_para_romano_string(self):
    self.assertEqual(
      numero_para_romano('3999'),
      "MMMCMXCIX"
    )

  def test_numero_para_romano_invalido(self):
    self.assertRaises(
      ValueError,
      numero_para_romano,
      0
    )

  def test_numero_para_romano_errado(self):
    self.assertNotEqual(
      numero_para_romano(8),
      "IIX"
    )

  def test_numero_para_romano_errado2(self):
    self.assertNotEqual(
      numero_para_romano(9),
      "VIIII"
    )

if __name__ == '__main__':
  unittest.main()

  