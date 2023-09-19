##Do arquivo functions.py importamos todas as funções
from functions import *

#Define os campos do CPF

numbers_cpf = int(input('Digite quantos CPF você quer gerar: '))
lista_cpf_gerados: []
for i in range(numbers_cpf):
    
    nove_primeiros = nine_first()
    penultimo_numero = validate_penultimate_number(nove_primeiros)
    ultimo_numero = validate_last_number(nove_primeiros)
    cpf = f"{nove_primeiros}{penultimo_numero}{ultimo_numero}"
    print(cpf)
    #lista_cpf_gerados.append(cpf)

