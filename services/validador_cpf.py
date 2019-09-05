import re

def retira_formatacao(num_cpf: str) -> str:
    """
    Limpa a formatação da string cpf
    "123-456-789.01 -> 12345678901" 
    """

    #Retira tudo que não é número da string
    num_cpf_limpo = re.sub('[^0-9]+', '', num_cpf)
    return num_cpf_limpo

def valida_cpf(num_cpf):
    """
    Valida um cpf
    "386-807-164.48" -> True
    "11111111111" -> False
    """

    #Transforma a string do cpf em uma lista de números
    digitos = [int(numero) for numero in retira_formatacao(num_cpf)]
    
    #Verifica o tamanho do cpf
    if len(digitos) != 11:
        return False

    #Verifica se todos os dígitos são iguais
    if len(set(digitos)) <= 1:
        return False

    #Validando o primeiro dígito verificador
    primeiro_digito_verificador = digitos[9]
    soma_dos_produtos = sum([a * b for a, b in zip(digitos[0:9], range(10, 1, -1))])
    digito_verificador_real = (soma_dos_produtos * 10 % 11) % 10 #Se o resto for 10, deve ser considerado como 0
    if primeiro_digito_verificador != digito_verificador_real:
        return False

    #validando o segundo dígito verificador
    segundo_digito_verificador = digitos[10]
    soma_dos_produtos = sum([a * b for a, b in zip(digitos[0:10], range(11, 1, -1))])
    digito_verificador_real = (soma_dos_produtos * 10 % 11) % 10
    if segundo_digito_verificador != digito_verificador_real:
        return False
    
    return True