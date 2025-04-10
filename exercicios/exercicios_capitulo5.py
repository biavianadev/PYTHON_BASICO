# Exercícios sobre o capítulo 5

# 1. Escreva um programa que permaneça em laço enquanto um valor X lido for diferente de zero. 
# Para cada valor de X apresente na tela se é par ou ímpar.
X = 1
while X != 0:
    X = int(input('Digite X: '))
    if X % 2 == 0:
        print(f'{X} é par')
    else:
        print(f'{X} é ímpar')
print("Fim do Programa")


# 2. Escreva um programa que mostre na tela a tabuada do número inteiro N que deve ser lido do teclado.
N = int(input('Digite N: '))
cont = 1
while cont <= 10:
    R = cont * N
    print(f'{cont} x {N} = {R}')
    cont = cont + 1
print('Fim do Programa')


# 3. Escreva um programa que mostre na tela os 10 primeiros termos de uma progressão aritmética (PA) com primeiro termo P e razão R. 
# Os dois números P e R são inteiros e devem ser lidos do teclado.
P = int(input("Digite o primeiro termo: ")) # linha 1
R = int(input("Digite a razão: "))
cont = 0
while cont < 10:
    print(P)
    P = P + R
    cont = cont + 1
print('Fim do Programa')


# 4. Escreva um programa que leia do teclado um número inteiro D. Esse número deve ser obrigatoriamente maior que zero. 
# Em seguida exiba na tela todos os números inteiros menores que 100 e que sejam divisíveis por D.
D = int(input('Digite D: '))
if D <= 0:
    print(f'O valor {D} é inválido')
else:
    i = 1
    while i < 100:
        if i % D == 0:
            print(i)
        i = i + 1
print('Fim do Programa')
