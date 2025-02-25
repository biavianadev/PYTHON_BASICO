# Comandos de Saída e Entrada - capítulo 3

# Função print() - exibe o que está entre parenteses
print('Esta é uma mensagem exemplo') # texto literal
X = 15
print(X) # objeto int()
Y = 28
print(Y)

print(X, Y) # exibirá os dois valores, com espaçamento sep = ' '
# alterando o sep
print(X, Y, sep="-") # pode ser qualquer separador

print('Valor de X =', X) # texto literal + valor do objeto


# Função .format()
A = 36
B = 48
s = "Valores: X = {0} e Y = {1}".format(X, Y)
print(s)
# outras formatações com .format()
X = 4.586
S = "Dado = {:d}".format(A)
print(S)
N = "Dado = {:f}".format(X)
print(N)


# Formatação utilizando f-string
C = 14
D = 32
s2 = f"Valores: C é {C} e D é {D}" # começar com "f"
print(s2)
# outras formatações com f-string
E = f"Dado = {A:d}"
print(E)
F = f"Dado = {A:f}"
print(F)


# O que é o "/n"
print('um\ndois') # pula uma linha


# Função input()
G = input('Digite algo: ') # o input vai esperar que algo seja digitado
print(G)
# input() + função de conversão
H = int(input('Digite H: '))
print(H)
type(H)
