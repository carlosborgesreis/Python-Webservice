import unittest
import re
from services.validador_cpf import *

class TestValidaCpf(unittest.TestCase):
  def test_retira_formatacao(self):
    self.assertEqual(
      retira_formatacao("123.456.789-01"),
      "12345678901" 
    )

  def test_retira_formatacao_limpo(self):
    self.assertEqual(
      retira_formatacao("12345678901"),
      "12345678901"
    )
  
  def test_retira_formatacao_tipo_errado(self):
    self.assertRaises(
      TypeError,
      retira_formatacao,
      1234567801
    )

  def test_retira_formatacao_vazio(self):
    self.assertEqual(
      retira_formatacao(""),
      ""
    )

  def test_valida_cpf_false(self):
    self.assertFalse(
      valida_cpf("11111111111")
    )

  def test_valida_cpf_true(self):
    self.assertTrue(
      valida_cpf("38680716448")
    )

  def test_valida_cpf_formatado(self):
    self.assertTrue(
      valida_cpf("386-807-164.48")
    )

  def test_valida_cpf_vazio(self):
    self.assertFalse(
      valida_cpf("")
    )

  def test_valida_tipo_errado(self):
    self.assertRaises(
      TypeError,
      valida_cpf,
      1234567801
    )

if __name__ == "__main__":
  unittest.main()
