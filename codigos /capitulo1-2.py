# Introdução Python - capítulos 1 e 2

# Comando de atribuição
print(a) # mensagem de ERRO - não foi atribuído valor ao objeto 'a'

b = 10 # atribuí ao objeto 'b' o valor '10'
print(b)


# Classes
c = 15
type(c) # é da classe inteiro - 'int'

d = 17.5
type(d) # é da classe reais - 'float'

obj1 = 'Hello world!'
type(obj1) # é da classe string - 'str'


# id dos objetos
obj2 = 20
obj3 = 30 - 10
print(obj2, obj3) # são idênticos
type(obj2)
type(obj3)
id(obj2)
id(obj3) # possuem o mesmo id, pois são idênticos

obj4 = 40 / 2
print(obj4)
type(obj4)
id(obj4) # será diferente, pois pertence à classe 'float'


# Objetos imutáveis e mutáveis
obj5 = 4
id(obj5)
obj5 = 10
id(obj5) # Será diferente, pois se trata de um objeto imutável

L = [44, 17, 26, 35, 20]
id(L)
L[0] = 12
print(L)
id(L) # será o mesmo, pois se trata de um objeto mutável


# Introdução Python - Expressões Aritméticas e Funções MatemáticasS

# Operações aritméticas
A = 14
B = 5
C = A + B # soma
print(C)
D = A - B # subtração
print(D)
E = A * B # multiplicação
print(E)
F = A / B # divisão
print(F)
G = A // B # divisão inteira
print(G)
H = A % B # resto da divisão
print(H)
I = -A # inverter o sinal
print(I)
J = A ** B # potência
print(J)


# Ordem das operações - utilizar parenteses para prioridade
a = 17
b = 14
c = a * 2 + b
print(c)
d = a * (2 + b)
print(d) # parenteses para prioridade


# Comando de Atribuição Incremental
A = 10
P = 4
A += P # equivale a A = A + P
print(A)
B = 0
B += 15 # equivale a B = B + 15
print(B)
C = 5
C -= 10 # equivale a C = C - 10
print(C)
D = 6
D *= 6 # equivale a D = D * 6
print(D)
E = 8
E /= 4 # equivale a E = E / 4
print(A)


#Funções Matemáticas
from math import sqrt # importação de função de biblioteca-padrão
X = 49
R = sqrt(X) # fornece a raíz da número
print(R)
