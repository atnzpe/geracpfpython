##Do arquivo functions.py importamos todas as funções
from functions import *

print(nine_first())
print(validate_penultimate_number(nine_first()))

nove_primeiros = nine_first()
penultimo_numero = validate_penultimate_number(nove_primeiros)

cpf = f"{nove_primeiros}{penultimo_numero}"

print(cpf)
print(cpf)


for i in range(10):
    nove_primeiros = nine_first()
    penultimo_numero = validate_penultimate_number(nove_primeiros)

    cpf = f"{nove_primeiros}{penultimo_numero}"

    print(cpf)
