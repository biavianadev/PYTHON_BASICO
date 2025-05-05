# Introdução Python (capítulo 1 e 2)

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

# Comandos de Entrada e Saída (capítulo 3)

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

# Comando Condicional (capítulo 4)

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

- Executa o bloco do primeiro `if` verdadeiro.
- Se nenhum `if`/`elif` for verdadeiro, executa o `else` (opcional).
- Pode haver múltiplos `elif`.

### Comandos Condicionais Alinhados

`if` dentro de outro `if` ou `else` são comuns. A indentação correta é essencial para evitar erros. Na pasta `codigos/capitulo4.py` verá um exemplo prático que como esse alinhamento funciona.

---------------------------------------

# Comandos de Repetição (capítulo 5)

## O Comando while

Estrutura: "enquanto a condição for verdadeira, execute o bloco".
Importante: a condição é testada antes da primeira execução.

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

Seu funcionamento ocorre assim: o laço é repetido normalmente enquanto a condição for **verdadeira**. Quando a condição se tornar **falsa** o laço termina e o código do `else` é executado. Se um comando `break` existir no laço e for executado, então o `else` não é executado.

--------------------------------------

# Tratamento de exceções (capítulo 6)

## Conceitos básicos

Exceções lidam com erros inesperados (como divisão por zero). Usar apenas `if` nem sempre é suficiente, afinal os sistemas estão cada vez mais complexos. 

### Tratamento de Exceções em Python – Forma Essencial

Usa-se `try-except`. Se ocorrer erro no `try`, o controle passa para o `except`.

### Tratamento de Exceções em Python - Forma Completa

Blocos possíveis:

- `try`: código protegido
- `except`: executado em caso de erro
- `else`: executado se não houver erro
- `finally`: sempre executado, usado para limpeza

---------------------------------------------

# Objetos Compostos (capítulo 7)

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

---------------------------------------------

`STATUS: em andamento`
