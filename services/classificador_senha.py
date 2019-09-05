import string

def classifica_senha(senha: str) -> int:
  """
  Classificador de senhas
  0 = Fraca
  1 = Media
  2 = Forte
  Fatores: existência de números ou caracteres especiais aumentam a força em 1 cada
  mas a senha precisa ter letras
  """
  
  if len(senha) == 0:
    return 0
    
  classificacao = -1

  if has_letters(senha):
    classificacao += 1
  if has_numbers(senha):
    classificacao += 1
  if has_special(senha):
    classificacao += 1

  return classificacao

def has_letters(senha) -> bool:
  letters = string.ascii_letters
  return any([char in letters for char in senha])

def has_numbers(senha) -> bool:
  return any([char.isdigit() for char in senha])

def has_special(senha) -> bool:
  return any([char in string.punctuation for char in senha])