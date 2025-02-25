# Comando Condicional - capítulo 4

# Expressa a condição de verdadeiro ou falso, definindo um valor ao objeto, em cada caso
A = int(input('Digite A: '))
B = int(input('Digite B: '))
if B == 0:
    print('Não é possível calcular a divisão')
else:
    R = A / B
    print(R)


# Condições Simples
A = 10
B = 50
# comparação entre objeto e literal
print(A > 0) # o resultado é True porque A é maior que zero
print(B <= 0) # o resultado é False porque B não é maior ou igual a zero
# comparação entre dois objetos
print(A >= B) # o resultado é False porque A não é maior ou igual a B
# comparação entre fórmula e objeto
print(5 * A == B) # o resultado é True porque 5 vezes A é igual a B
# comparação entre objeto e função (raiz quadrada de B)
print(A >= pow(B, 0.5)) # o resultado é True porque A é maior ou igual à raiz de B


# Negações e Condições Compostas
x = 10
y = 5
z = 0
print((x > y) and (y > z)) # True, pois ambas as condições são verdadeiras
print((x < y) or (z == 0)) # True, pois uma das condições é verdadeira
print(not (x == y)) # True, pois x não é igual a y
# condições compostas mistas
C = 15
D = 9
E = 9
print(D == E or C < D and C < E) # será True, pois começa pelo 'and' e depois 'or'
print((D == E or C < D) and C < E) # será False, pois começa pelo 'or' e depois 'and'


# Retomada Comando Condicional
PH = float(input("Digite um valor do PH: "))
if PH < 6.0:
    r = "ácida"
elif PH < 7.0:
    r = "levemente ácida"
elif PH == 7.0:
    r = "neutra"
elif PH < 8.0:
    r = "levemente alcalina"
else:
    r = " alcalina"
print(f'Com pH = {PH} a solução é {r}')

# Comandos Condicionais Alinhados
risco = input('Digite BX ou AL para o grau de risco: ')
if risco != 'BX' and risco != 'AL':
    print(f'{risco} é inválido para o grau de risco')
else:
    valor = float(input('Digite o valor: '))
    if risco == 'BX':
        if valor < 1000.0:
            tipo = 'Poupança'
        else:
            tipo = 'Renda fixa'
    else: # risco == 'AL'
        if valor < 1000.0:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'
    print(f'Você deve investir em {tipo}')
