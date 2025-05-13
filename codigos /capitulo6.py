# Tratamento de exceções - capítulo 6

# Tratamento de Exceções em Python – Forma Essencial
A = int(input('Digite A: '))
B = int(input('Digite B: '))
try:
    R = A / B
    print(f'Resultado = {R}')
except:
    print('Não é possível calcular a divisão')
