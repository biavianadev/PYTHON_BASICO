# Introdução Python (capítulo 1 e 2)
## Classes e Objetos
As _classes_ e _objetos_ são conceitos fundamentais da programação orientada a objetos (POO) em Python. Eles são importantes porque permitem criar programas mais organizados, reutilizáveis e fáceis de manter. Segue um resumo sobre cada um dos termos:
- Classe é um modelo que define o estado e comportamento dos **objetos**.
- Objeto é construído a partir da materialização de uma **classe**. Os objetos podem ser _simples_ ou _compostos_ e _mutáveis_ ou _imutáveis_.
  
## Comando de Atribuição
O comando de atribuição é um elemento de programação muito simples e necessário existente em todas as linguagens. 

A forma geral do comando de atribuição é esta: `identificador = expressão`

A expressão do lado direito pode ser uma das seguintes possibilidades:
- um literal (um valor fixo numérico ou texto); ex: a = 10 ou m = 'texto'
- um objeto; ex: b = a
- uma fórmula matemática; c = a + 10
- uma função; d = len('exemplo')
- ou ainda uma expressão com uma combinação dos itens acima.
  
## Id dos Objetos
Todo objeto Python é associado a um número inteiro único gerado no momento da criação do objeto e que é mantido constante durante todo o tempo em que o objeto existir. A função interna `id()` é usada para exibi-lo.

Cada vez que o interpretador Python precisar processar um comando de atribuição "=", ele vai avaliar a expressão e determinar a classe e um conteúdo para o objeto, em seguida verificará que se já existe um id que satisfaça essa combinação: se existir, ele faz a associação do identificador com o número **id**; se não existir, ele cria um **id** para o novo objeto.

### Objetos Imutáveis e Mutáveis
Os objetos em Python são classificados em duas categorias: _imutável_ e _mutável_. Compreender a distinção entre essas duas categorias de objetos em Python é fundamental para criar um código livre de erros e que também seja eficiente e confiável. Segue um resumo sobre cada um dos termos:
- Objetos imutáveis

Em termos práticos: quando um objeto é imutável, depois de criado, se for preciso trocar seu conteúdo o objeto antigo é descartado e um novo é criado.
`Números inteiros, números reais, strings, tuplas entre outros são imutáveis`
- Objetos mutáveis

Os objetos mutáveis são o outro lado dessa ideia. Ou seja, são aqueles cujo conteúdo pode ser alterado após serem criados. O id desses objetos se mantém o mesmo durante toda a vida dele enquanto seu conteúdo pode ser livremente alterado sempre que necessário.
 `Os objetos mutáveis são tipicamente as listas, dicionários e conjuntos`

## Expressões Aritméticas
Em Python, as expressões são construídas utilizando-se objetos de classes numéricas, operadores aritméticos e funções matemáticas. Uma expressão aritmética é algo como essa linha: 

`R = A + B` 

onde: A e B são objetos numéricos e R recebe o resultado de sua adição. Nessa expressão, A e B são chamados de operandos e " + " é o operador aritmético de adição.
- Havendo, em uma expressão, a mistura de operandos inteiros e reais, o resultado calculado será real. E quando houver inteiros, reais e complexos, o valor resultante será tratado como complexo.

### Comando de Atribuição Incremental
Uma forma muito frequente de expressão aritmética usada nos algoritmos é aquela em que se toma o conteúdo de um objeto e a ele se soma um certo valor ou outra variável. Uma expressão assim é escrita assim:

`A = A + 1`

Para compreender esta expressão primeiro deve-se olhar para seu lado direito: o interpretador irá executar o cálculo `A + 1` e produzir um resultado. Esse resultado será atribuído ao objeto presente no lado esquerdo da expressão, que é o próprio **A**. Assim, haverá a substituição do valor original pelo novo valor calculado.

Em Python, nestes casos, pode-se usar a operação de atribuição incremental, que tem a seguinte construção: `A += 1`

## Funções Matemáticas
Junto com os operadores aritméticos já apresentados, na linguagem Python pode-se utilizar uma gama muito grande de funções matemáticas. 

Parte dessas funções estão na biblioteca-padrão e outra parte está em duas bibliotecas externas: `math` contém funções matemáticas que se aplicam a valores numéricos inteiros e reais; `cmath` contém funções matemáticas que se aplicam a números complexos. Ambas nos fornecem uma grande variedade de funções prontas.

---------------------------------------------

# Comandos de Entrada e Saída (capítulo 3)
## Função print()
A função print() é uma das funções internas de Python 3 e seu propósito é realizar operações de saída de dados. 
- Saída de dados é exibir na tela ou gravar em um arquivo os conteúdos (valores) dos objetos que estão na memória do computador. Assim, pense que o print() é o modo mais básico existente em Python para que o programa "forneça resultados" para quem o está utilizando.

### Função .format()
Para produzir uma sequência formatada, o primeiro passo é definir como se quer o texto final, tomando o cuidado de utilizar os marcadores {0}, {1}, {2} etc. nos pontos onde se deseja que apareça o conteúdo dos objetos envolvidos. O texto deve ser seguido do método .format(), que conterá como argumentos os objetos que fornecerão os valores que serão usados para substituir os marcadores.

Adicionalmente, os marcadores podem receber qualificadores de formatação que definem aspectos de como os dados devem ser formatados. Isso é feito através do uso do caractere ":" (dois pontos) dentro dos marcadores.

São comuns três qualificadores de formatação para os seguintes aspectos:
- Tipo de apresentação: inteiro decimal, binário ou hexadecimal; real; caractere;
- Tamanho da apresentação: quantidade total de caracteres a serem usados e opcionalmente quantidade de casas decimais para os números reais;
- Alinhamento da apresentação: é possível especificar se um dado será alinhado à esquerda, à direita ou centralizado;

Pra saber mais sobre as formatações, acesse o link: https://docs.python.org/pt-br/3/library/string.html#formatspec

### Formatação usando f-string
O segundo modo de formatação é chamado de f-string (uma abreviação para o nome oficial "formatted string literals"). Este modo foi introduzido na versão 3.6 se Python e rapidamente se tornou muito popular pois faz o mesmo que o método .format(), porém com uma forma de escrita mais clara e compacta.

Um f-string começa com uma das letras "f" ou "F" e dentro do marcador {} é colocado o objeto que se quer exibir naquela posição: `s2 = f"Valores: A é {A} e B é {B}"`

### O que é o /n
Ao usar a função print() é muito comum nos depararmos com a dupla de caracteres \n, encontrada em várias linguagens de programação. Na verdade, porém, não se trata de uma dupla de caracteres: o \n é uma "sequência de escape" (escape sequence). Sequências de escape consistem em uma barra invertida (\) seguida de uma letra ou dígitos e representam determinadas ações, como no caso do \n que representa a ação de "pulo de linha" ou "avanço de linha".

Para saber mais sobre sequências de escape, acesse o link: https://learn.microsoft.com/pt-br/cpp/c-language/escape-sequences

## Função input()
É preciso que exista alguma forma de permitir que dados sejam digitados no teclado do computador e inseridos em objetos do programa. Em Python 3 quem realiza essa tarefa é a função input(). Para usá-lo basta atribuir seu retorno a algum identificador. Opcionalmente pode-se passar um parâmetro que será usado como uma mensagem que indique o que deve ser digitado.

Quando a função `input()` é executada o computador aguarda que o usuário digite o que precisar seguido de "Enter". Quando a tecla "Enter" é pressionada tudo o que foi digitado é carregado no objeto que recebe o retorno da função. O usuário pode digitar o que quiser e a leitura sempre resulta em uma cadeia de caracteres (string) carregada no objeto de destino.

### Uso conjunto do input com Funções de Conversão
É muito comum que nos programas seja necessário ler números inteiros e reais. Como a função input() sempre lê strings, será necessário executar uma conversão depois da leitura, para facilitar, isso pode ser feiro em apenas uma etapa:

Exemplo de input com conversão da classe string() para int(): `A = int(input('Digite A: '))`

---------------------------------------------
`STATUS: em andamento`
