#Cria a função de nome nine_first para obter os 9 primeiros digitos
def nine_first():
    #Importa biblioteca random
    import random
    #Cria uma variável vazia, chamada nine_digits para armazenar os 9 digitos
    nine_digit = ''
    #Executa um for  com um range de tamanho 9 para alimentar a variável nine_digit
    for i in range(9):
        #A cada iteração adicione um numero aleatorio entre 0 e 9 dentro da variavel nine_digit
        nine_digit += str(random.randint(0,9))
    #retorna o valor da varialvel nine_digit         
    return nine_digit

#Cria função para validar o penultimo numero do cpf
def validate_penultimate_number(nine_numbers):
    #Contador regressivo
    countdown = 10
    #Cria uma lista para armazenar os multiplos dos nove primeiros numeros
    nine_first_numbers = []
    #Percorre o CPF multiplicando cada item por um contador regressivo que alimenta a lista
    for i in nine_numbers:
        #Numero multiplicado por contador regressivo
        number_multiplies_by_ten = int(i)*(countdown)
        #Adicona o numero multplicado por 10 a lista
        nine_first_numbers.append(number_multiplies_by_ten)
        #Decrementa o contador
        countdown -=1

    #Faz a soma de todos os itens da lista
    sum_nine_first_numbers = sum(nine_first_numbers)
    #Multipicla a variavel que soma os itens por 10
    multiplie_sum_nine_first_numbers = sum_nine_first_numbers * 10
    #Obter o resto da divisão de multiplie_sum_nine_first_numbers por 11
    resto_multiplie = multiplie_sum_nine_first_numbers % 11
    #Defina o penultimo numero
    result = resto_multiplie if resto_multiplie <= 9 else 0
    #retorna result
    return result

#Cria função para validar o último numero do cpf
def validate_last_number(nine_numbers):
    #Contador regressivo começando em 11
    countdown = 11
    #Cria uma lista para armazenar os multiplos dos nove primeiros numeros
    nine_first_numbers = []
    #LIsta dos 9 primeiros e o primeiro numero
    nine_numbers = nine_first()
    penultible_number = validate_penultimate_number(nine_first())
    nine_first_numbers_and_first = list(f'{nine_numbers}{penultible_number}')
    #Lista dos numeros multiplicados pelo contador regressivo
    nine_numbers_and_first_number_multiple_countdow = []

    #laco for para percorrer e multiplicar   
    for i in nine_first_numbers_and_first:
        number_multiplies_by_eleven = int(i)*(countdown)
        nine_numbers_and_first_number_multiple_countdow.append(number_multiplies_by_eleven)
        countdown -=1

    #Printa a soma da lista
    soma_lista = sum(nine_numbers_and_first_number_multiple_countdow)

    #Multiplica o resultado por 10
    multi_list_for_ten = soma_lista * 10

    #Obtem o resto da divisão da conta anterior por 11
    div_sum_anterior = multi_list_for_ten % 11

    result = div_sum_anterior if div_sum_anterior <= 9  else 0

    #Retorna o resultado
    return result


#final = 