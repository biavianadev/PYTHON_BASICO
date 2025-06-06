# Introdução Python - capítulo 1 e 2

## Classes e Objetos

- Classe: modelo que define o estado e comportamento de **objetos**.

- Objeto: materialização de uma **classe**; pode ser _simples/composto_ e _mutável/imutável_.

## Comando de Atribuição

Atribui valores a identificadores:

`identificador = expressão`

A expressão pode ser:
- um literal (um valor fixo numérico ou texto): `a = 10` ou `m = 'texto'`
- um objeto: `b = a`
- uma fórmula matemática: `c = a + 10`
- uma função: `d = len('exemplo')`
- ou ainda uma expressão com uma combinação dos itens acima.

## Id dos Objetos

Todo objeto Python é associado a um número inteiro único (id), que pode ser exibido com a função `id()`. O interpretador avalia a expressão, reutiliza ids caso algum satisfaça a combinação, ou cria novos.

### Objetos Imutáveis e Mutáveis

- Imutáveis: não podem ser alterados (ex.: int, float, str, tuple).
- Mutáveis: podem ser modificados (ex.: list, dict, set). Seu `id` se mantém o mesmo, por mais que seu conteúdo seja alterado.

## Expressões Aritméticas

São compostas por operandos e operadores (ex.: `R = A + B`). Em caso de mistura de tipos, resulta no tipo mais abrangente (real > inteiro, complexo > real).

### Comando de Atribuição Incremental

Forma simplificada: `A += 1` (equivale a `A = A + 1`).

## Funções Matemáticas

Disponíveis em bibliotecas:

- `math` (valores reais e inteiros)
- `cmath` (números complexos)

------------------------------------------

# Comandos de Entrada e Saída - capítulo 3

## Função print()

Realiza operações de saída de dados, ou seja, exibe dados na tela ou grava em arquivos.

### Função .format()

Usa marcadores `{}` com `.format()`. Pode incluir qualificadores de tipo, tamanho e alinhamento.

Pra saber mais sobre as formatações, acesse o link: https://docs.python.org/pt-br/3/library/string.html#formatspec

### Formatação usando f-string

Sintaxe mais simples que `.format()` (ex.: `f"Valores: A é {A} e B é {B}"`).

### O que é o \n

`\n` é uma sequência de escape que representa uma quebra de linha.

Para saber mais sobre sequências de escape, acesse o link: https://learn.microsoft.com/pt-br/cpp/c-language/escape-sequences

## Função input()

Lê dados do teclado (sempre como string). Pode incluir uma mensagem (ex.: `input('Digite algo: ')`).

### Uso conjunto do input com Funções de Conversão

Conversão direta ao ler (string() para int()):

Ex.: `A = int(input('Digite A: '))`

----------------------------------------

# Comando Condicional - capítulo 4

## Conceito Geral

O comando condicional `if-else` permite que o programa tome decisões com base em condições lógicas. Exemplo: evitar divisão por zero com `if B == 0`.

### Indentação

  A indentação indica hierarquia de blocos de código. Em Python, ela é obrigatória, especialmente em estruturas como `if`, `else`, `while`, `for`, `def`, etc.

## Condições Simples

Condicional com operadores relacionais:

- `==`, `!=`, `<`, `<=`, `>`, `>=`

Estrutura básica: `<expressão 1> <operador> <expressão 2>`

As expressões 1 e 2 podem ser:
- Um valor literal (como um número ou texto)
- Um objeto
- Uma fórmula (expressão aritmética)
- Uma chamada de função

## Negação e Condições compostas

Operadores lógicos:

- `not` (negação)
- `and` (e)
- `or` (ou)

Em caso de uma condição composta mista, o programa segue essa sequência: `not` > `and` > `or`. Parênteses podem alterar essa ordem.

## Comando Condicional - Forma Completa

O comando `if-elif-else` permite testar várias condições:

```python
if <condição 1>:
    <bloco de comandos 1>
elif <condição 2>:
    <bloco de comandos 2>
elif <condição 3>:
    <bloco de comandos 3>
else:
    <bloco de comandos do else>
```

- Executa o bloco do primeiro `if` verdadeiro.
- Se nenhum `if`/`elif` for verdadeiro, executa o `else` (opcional).
- Pode haver múltiplos `elif`.

### Comandos Condicionais Alinhados

`if` dentro de outro `if` ou `else` são comuns. A indentação correta é essencial para evitar erros. Na pasta `codigos/capitulo4.py` verá um exemplo prático que como esse alinhamento funciona.

---------------------------------------

# Comandos de Repetição - capítulo 5

## O Comando while

Estrutura: "enquanto a condição for verdadeira, execute o bloco".
Importante: a condição é testada antes da primeira execução.

```python
while <condição>:
    <conjunto de comandos>
```

Elementos de um laço:

- **Inicialização:** situação inicial do controle do laço;
- Condição de continuidade do laço;
- **Iteração:** ação sobre o controle do laço, a cada repetição; e
- **Corpo:** bloco de código subordinado.

## Comando continue

Interrompe a execução atual e passa para a próxima repetição.

## Comando break

Interrompe o laço imediatamente.

## Cláusula else do comando while

Em Python a forma completa do comando `while` inclui uma parte `else`. 

```python
while <condição>
    <bloco de comandos 1 – que pode conter um break>
else:
    <bloco de comandos 2>
```

Seu funcionamento ocorre assim: o laço é repetido normalmente enquanto a condição for **verdadeira**. Quando a condição se tornar **falsa** o laço termina e o código do `else` é executado. Se um comando `break` existir no laço e for executado, então o `else` não é executado.

--------------------------------------

# Tratamento de Exceções - capítulo 6

## Conceitos básicos

Exceções lidam com erros inesperados (como divisão por zero). Usar apenas `if` nem sempre é suficiente, afinal os sistemas estão cada vez mais complexos. 

### Tratamento de Exceções em Python – Forma Essencial

Usa-se `try-except`. Se ocorrer erro no `try`, o controle passa para o `except`.

```python
try:
    <bloco de código protegido>
except:
    <bloco de tratamento da exceção>
```

### Tratamento de Exceções em Python - Forma Completa

Blocos possíveis:

```python
try:
    <bloco 1>
except:
    <bloco 2>
else:
    <bloco 3>
finally:
    <bloco 4>
```

- `try`: código protegido
- `except`: executado em caso de erro
- `else`: executado se não houver erro
- `finally`: sempre executado, usado para limpeza

---------------------------------------------

# Objetos Compostos - capítulo 7

## Conceito Geral

Objetos compostos (ou estruturados) são fundamentais em Python, pois:

- Permitem manipular grandes volumes de dados com eficiência e flexibilidade.
- Seu conteúdo é acessível tanto individualmente quanto em grupo.

Entre os objetos compostos, destacam-se os Objetos Sequenciais:

- `Strings` (classe str)
- `Listas` (classe list)
- `Tuplas` (classe tuple)

Esses objetos têm elementos organizados por índices numéricos iniciando em 0 (da esquerda para a direita). A indexação é feita com colchetes `[ ]`.

## Listas – classe list 

- São sequências que armazenam objetos de qualquer classe.
- Exibição pode ser feita com `print(lista)` ou por laço com `print(lista[i])`.

Podem ser:

  - **Homogêneas**: elementos de uma única classe.
  - **Heterogêneas**: elementos de diferentes classes.

## Operações com Listas 

### Indexação

- Acesso via índices inteiros: `lista[0]`, `lista[1]`, etc.
- Índices negativos acessam de trás para frente: `lista[-1]`, `lista[-2]`, etc.
- Acesso fora dos limites gera `IndexError`.

### Eliminação de elementos

- Usa-se a função `del`: `del lista[i]` remove o elemento do índice i.

### Fatiamento (slicing)

Permite criar sublistas a partir de outra lista:

- Sintaxe: `nova_lista = lista[ini:fim]` (exclui o índice `fim`)
- Com passo: `nova_lista = lista[ini:fim:passo]`

Parâmetros podem ser omitidos:

  - `lista[:fim]` – do início até fim-1
  - `lista[ini:]` – de ini até o fim

### Cópia de listas

- Atribuição direta (`B = A`) copia apenas a referência, não os dados. Para cópia real (nova lista), use slicing: `B = A[:]`

### Operador in

- Verifica se um valor está na lista: `x in lista`
- Pode ser negado: `x not in lista`
- Funciona com outros objetos compostos além de listas.

## A classe range

### Conceito

Apesar de ser chamada com parênteses, `range` não é uma função, e sim um tipo sequencial imutável. Serve para criar sequências de números inteiros comumente usadas em laços de repetição.

### Sintaxe geral

`range(start, stop[, step])`

- **start:** valor inicial (opcional, padrão é 0)
- **stop:** valor final (obrigatório, mas não incluído na sequência)
- **step:** passo (opcional, padrão é 1)

Exemplos:

```python
range(10) → [0, 1, ..., 9]  
range(3, 8) → [3, 4, 5, 6, 7]  
range(5, 12, 3) → [5, 8, 11]
```

**Observações:**

- Para exibir os valores da sequência na tela, é necessário convertê-la com `list()`.
- Exemplo: `print(list(range(5, 12, 3)))`
- Para incluir o último valor na sequência, é comum usar:
  `range(início, último+1, passo)`

## O comando for 

### Conceito

`for` é um comando de repetição específico para iterar sobre objetos estruturados como:

- listas, strings, tuplas, dicionários, conjuntos e objetos `range`.

### Estrutura geral

```python
for objctrl in objseq:
    bloco1
else:
    bloco2
```

Funcionamento:

1. objseq é verificado como iterável.
2. objctrl recebe um valor por vez de objseq.
3. bloco1 é executado para cada valor.
4. Se o laço terminar normalmente, bloco2 (else) é executado.

**Comandos adicionais:**

- `continue`: interrompe a repetição atual e passa ao próximo item.
- `break`: encerra o laço imediatamente (impede a execução do else).

### Uso comum:

```python
for i in range(5):
    print(i)
```

## Operadores com Classes Sequenciais 

### Concatenação com "+"

Une duas sequências do mesmo tipo (listas, tuplas ou strings).

Exemplo:

```python
A = [10, 12]
B = [20, 22]
R = A + B  → [10, 12, 20, 22]
```

### Multiplicação com "\*"

Repete uma sequência várias vezes.

Exemplos:

```python
A = [1, 2, 3] * 3  → [1, 2, 3, 1, 2, 3, 1, 2, 3]  
B = [0] * 10       → [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Tuplas – classe tuple

### Conceito

`Tuplas` são sequências **imutáveis**, ou seja, seus elementos não podem ser alterados após a criação. São usadas principalmente para armazenar dados heterogêneos (como diferentes tipos de dados), embora também possam ser homogêneas.

### Aplicações comuns

- Representar coordenadas `(x, y)`, como em gráficos e jogos.
- Armazenar cores em formato `RGB`.
- Guardar registros fixos como (matrícula, nome, idade) em bancos de dados.

### Características principais

- **Imutabilidade:** não podem ser modificadas após criadas.
- Consomem menos memória que listas.
- **Sintaxe:** podem ser criadas com ou sem parênteses.
  Exemplo: `T = (10, "azul", 3.14)`; `V = (1, 2, 3)`; `U = 5`, `"verde"`, `True`
- Suportam indexação, iteração (com for), e conversão para listas e vice-versa.

## String - classe str

### Conceito

`Strings` são sequências de caracteres (textos), pertencentes à classe str. São extremamente comuns em qualquer programa, desde os mais simples até os mais avançados.

### Observações

- São **imutáveis**.
- Suportam os mesmos comportamentos de outras sequências: indexação, fatiamento, iteração, concatenação.
- Para mais métodos específicos, consultar a documentação oficial do Python, pelo link: https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods

## Características comuns a listas, tuplas e strings

- **Ordenadas**: mantêm a ordem dos elementos conforme inseridos.
- **Indexáveis**: permitem acessar elementos por índices inteiros iniciando em zero.
- **Aninháveis**: podem conter outras sequências. Ex.: lista de listas, tupla de tuplas, etc.
- **Iteráveis**: podem ser percorridas com for ou compreensões de listas.
- **Fatiáveis**: suportam fatiamento para extrair subconjuntos.
- **Combináveis**: aceitam concatenação com o operador +.

---------------------------------------------

`STATUS: finalizado`  
> códigos finalizados

> exercícios em andamento
