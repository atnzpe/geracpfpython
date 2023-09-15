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

