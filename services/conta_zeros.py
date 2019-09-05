import re

def conta_zeros(texto) -> int:
    """
    Função que retorna a maior quantidade de zeros adjacentes em uma string qualquer
    "200030": str -> 3: int 
    """
    if type(texto) != str:
        raise TypeError("Inserir apenas strings!")

    #Encontra as ocorrências de zeros adjacentes com expressão regular
    adj_zeros = re.finditer(r'0+', texto)
    
    #Conta o tamanho das ocorrências
    quantidades = [len(zeros.group(0)) for zeros in adj_zeros]

    if len(quantidades) != 0:
        return max(quantidades)
    else:
        return 0