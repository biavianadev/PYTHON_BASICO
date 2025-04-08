# Comandos de Repetição - capítulo 4

# Comando while
print("Início do Programa")
cont = 1
while cont <= 10: 
    print(cont)
    cont = cont + 1 
print("Fim do Programa")


# Comando continue
i = 0
while i < 5:
     i = i + 1
     if i == 4:
         continue # a execução é imediatamente retornada ao cabeçalho do comando de repetição
print(i)


# Comando break
X = 1
while True:
    X = int(input('Digite X: '))
    if X == 0:
        print(' você digitou zero...')
        break # quando o break é executado o laço termina imediatamente
    print(X)
print('Fim do Programa')


# Cláusula else do Comando while
X = 1
while X > 0: # enquanto X for positivo faça as repetições
    X = int(input('Digite X: '))
    if X == 0: # se X for zero interrompa o laço
        print(' você digitou zero...')
        break
    print(X)
else: # este else é executado quando X for negativo se X for zero não
    print('você digitou negativo')
print('Fim do Programa') 
