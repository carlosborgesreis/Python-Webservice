import unittest
from services.classificador_senha import classifica_senha

class TestClassificadorSenha(unittest.TestCase):
  def test_classifica_senha_fraca(self):
    self.assertEqual(
      classifica_senha('aaaaaaaa'),
      0
    )

  def test_classifica_senha_fraca_2(self):
    self.assertEqual(
      classifica_senha('12345678'),
      0
    )

  def test_classifica_senha_fraca_3(self):
    self.assertEqual(
      classifica_senha('abcdefgh'),
      0
    )

  def test_classifica_senha_fraca_4(self):
    self.assertEqual(
      classifica_senha('AbCdEfGh'),
      0
    )

  def test_classifica_senha_media(self):
    self.assertEqual(
      classifica_senha('AbCdEfGh123'),
      1
    )

  def test_classifica_senha_media_2(self):
    self.assertEqual(
      classifica_senha('abcdEfgh123'),
      1
    )

  def test_classifica_senha_forte(self):
    self.assertEqual(
      classifica_senha('abcdEfgh123@!'),
      2
    )

  def test_classifica_senha_forte_2(self):
    self.assertEqual(
      classifica_senha('Abc123#@'),
      2
    )

  def test_classifica_senha_fraca_vazia(self):
    self.assertEqual(
      classifica_senha(''),
      0
    )

  def test_classifica_senha_tipo_errado(self):
    self.assertRaises(
      TypeError,
      classifica_senha,
      123456543
    )

if __name__ == '__main__':
  unittest.main()
