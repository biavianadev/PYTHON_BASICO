# Exercícios sobre o capítulo 4

# 1. Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
x = int(input('Digite um número: '))
if x % 2 == 0:
    print(f'O número {x} é par')
else:
    print(f'O número {x} é ímpar')


# 2. Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois. Se ambos forem iguais, mostre qualquer um deles.
y = int(input('Digite o primeiro número: '))
z = int(input('Digite o segundo número: '))
if y < z:
    print(f'O menor número é {y}')
elif z < y:
    print(f'O menor número é {z}')
else:
    print(f'Os dois números são iguais e valem {y}')


# 3. Escreva um programa que leia a idade de uma pessoa e mostre se está de acordo ou não com a classificação indicativa de 16 anos.
w = int(input('Digite a sua idade: '))
if w >= 16:
    print('Você está de acordo com a classificação de 16 anos')
else:
    print('Você não está de acordo com a classificação de 16 anos')


# 4. Escreva um programa que leia um número inteiro e mostre na tela se ele é divisível por 10 ou não.
n = int(input('Digite um número: '))
if n % 10 == 0:
    print(f'O número {n} é divisível por 10')
else:
    print(f'O número {n} não é divisível por 10')
