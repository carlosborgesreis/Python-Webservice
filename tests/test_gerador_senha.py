import unittest
from services.gerador_senha import *

class TestGeradorSenha(unittest.TestCase):
  def setUp(self):
    self.lista_senhas = [gera_senha() for i in range(100000)]
    self.menor_senha = min(self.lista_senhas, key=len)
    self.maior_senha = max(self.lista_senhas, key=len)

  def test_gerador_senha_tamanho_min(self):
    self.assertTrue(
      len(self.menor_senha) >= 8  
    )

  def test_gerador_senha_tamanho_max(self):
    self.assertTrue(
      len(self.maior_senha) <= 15
    )

  def test_gerador_senha_rand(self):
    self.assertTrue(
      len(set(self.lista_senhas)) == len(self.lista_senhas)
    )

if __name__ == "__main__":
  unittest.main()