# Gerador de CPF

## Ideia basica para gerar automaticamente CPF na linguagem Python

*Creditos*
https://gbtech.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34637012#overview



#### Cáculo do Primeiro Dígito CPF
CPF: 746.824.890-70

* Colete a soma dos 9 primeiros digitos so CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10.

Ex.: 746.824.890-70 (746824890)
...10..9..8..7..6..5..4..3..2
*..7...4..6..8..2..4..5..0..0
...70..36.48.56.12.20.32.27.0

* Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

* Multiplicar o resultado anterior por 10
301 * 10 = 3010

* Obter o resto da divisão da conta anteriro por 11
3010 % 11 = 7

* Se o resultado for maior que 9:
    resultado é 0
* contrario disso:
    resultado é o valor da conta



#### Calcular o Segundo Digito do CPF
CPF: 746.824.890-70

* Colete a soma dos 9 primeiros digitos do CPF, MAIS O PRIMEIRO DIGITO, 
multiplicando cada um dos valores por uma contagem regressiva começando de 11.

EX. 746.824.890-70 (7468248907)
...11.10..9..8..7..6..5..4..3..2
*..7...4..6..8..2..4..8..9..0..7.<--.PRIMEIRO.DIGITO
...77..40.54.64.14.24.40.36.0..14

* Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363

* Multiplica o resultado anteriro por 10
363 * 10 = 3630

* Obter o resto da divisão da conta anteriro por 11
3630 % 11 = 0

* Se o resultado anterior for maior que 9:
    resultado é 0
* contrário disso:
    resultado é o valor da conta

