import random
import string

def gera_senha() -> str:
  """
  Gera uma senha aleatória
  """
  tam_list = range(8, 16)
  chars = string.ascii_letters + string.digits + string.punctuation
  tamanho = random.choice(tam_list)
  senha = ''.join([random.choice(chars) for i in range(tamanho)])
  return senha

def main():
  for i in range(10):
    print(gera_senha())

if __name__ == "__main__":
  main()
