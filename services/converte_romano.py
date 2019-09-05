from collections import OrderedDict

ROMAN_MAP = OrderedDict([
  (1000, 'M'),
  (500,  'D'),
  (100,  'C'),
  (50,   'L'),
  (10,   'X'),
  (5,    'V'),
  (1,    'I')
])

def valida_numero(num):
  """
  Valida um número a ser convertido em romano
  0 < num < 4000
  """
  num = int(num)
  return 0 < num and num < 4000

def numero_para_romano(num):
  """
  Converte um número inteiro em algarismos romanos
  9 -> IX
  3999 -> MMMCMXCIX
  """

  global ROMAN_MAP
  num = int(num)
  result = []

  #Joga uma exception caso o número não seja válido
  if not valida_numero(num):
    raise ValueError("Inserir apenas valores inteiros entre 1 e 3999")
  
  i_anterior, r_anterior = first(ROMAN_MAP)
  for i, r in ROMAN_MAP.items():
      fator = num // i
      msd = most_significant_decimal(num)
      diff = abs(i - msd)
      diff_anterior = abs(i_anterior - msd)
      if has_roman(diff) and not has_roman(msd):
          result.append(ROMAN_MAP[diff] + r)
          num = num - msd
      elif num > i and has_roman(diff_anterior):
          result.append(ROMAN_MAP[diff_anterior] + r_anterior)
          num = num - msd
      else:
          result.append(r * fator)
          num = num - (fator * i)
      i_anterior, r_anterior = i, r
      if num == 0:
          break
  return ''.join(result)


# ------------------- Funções auxiliares:

def has_roman(num):
    global ROMAN_MAP
    for key_num, roman in ROMAN_MAP.items():
        if num == key_num:
            return True
    return False

def first(obj):
    return next(iter(obj.items()))

def most_significant_decimal(num):
    int_len = len(str(num))
    msd = str(num)[0].ljust(int_len, '0')
    return int(msd)

