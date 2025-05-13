# Objetos Compostos - capítulo 7

# Listas – Classe list
L = [] # criação da lista utilizando []
type(L)
L.append(3.88) #inclusão de objetos no final da lista
L.append(17.5) #inclusão de objetos no final da lista
print(L)
type(L[0])


# Formas de Indexação - exibe o elemento correspondente a sua posição (começa por [0])
A = [10, 12, 14, 16]
i = 0
print(A[i])
print(A[i+1])
print(A[i+2])

# utilizando o sinal de "-" antes do número, a ordem de indexação começa do último elemento
print(A[-1]) # último elemento da lista
print(A[-2]) # penúltimo elemento da lista


# Eliminação de Elementos com a Função del
del A[0] # elimina o primeiro elemento da lista A
print(A)


# Fatiamento de Listas
Origem = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
Destino1 = Origem[3:6]
print(Destino1) # primeiro caso

Destino2 = Origem[1:7:2]
print(Destino2) # segundo caso – incluindo o passo

Destino3 = Origem[:4]
print(Destino3) # terceiro caso – omitindo ini

Destino4 = Origem[6:]
print(Destino4) # quarto caso – omitindo fim


# Operador in
L = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print(25 in L) # 25 está em L, então in retornou True

print(99 in L) # 99 não está em L, então in retornou False

print(25 not in L) # 25 está em L, então not in retornou False

print(99 not in L) # 99 não está em L, então not in retornou True


# O Comando for

L = [21, 45, 17, 28]
pos = 0
for valor in L:
    print(f'A posição {pos} contém {valor}')
    pos += 1
print('Fim do Programa')


# Uso Combinado do range e for
for i in range(4):
    print(f'Valor i da vez = {i}')
print('Fim do Programa')


# Operadores de Concatenação e Multiplicação Aplicado a Classes Sequenciais

# Concatenação com "+"
A = [10, 12, 14, 16]
B = [20, 22, 24]
R = A + B # operador de concatenação '+' usado para juntar duas listas
print(R)

# Multiplicação com "*"
A = [1, 2, 3] * 3
print(A)
B = [0] * 10
print(B)


#Tuplas - classe tuple
T = (12, 'Python', 27.3, 14)
type(T)
U = 12, 'Python', 27.3, 14
type(U)
V = (10, 12, 14, 16)
type(V)
print(T[0])
print(T[1])
