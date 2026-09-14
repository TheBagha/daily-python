# Dia 3

## Objetivo

- Aprender a usar operadores aritméticos, relacionais e de atribuição em Python.
- Entender como realizar cálculos, comparar valores e atualizar variáveis.

## Anotações

### `Operadores`

Operadores são símbolos usados para fazer operações com valores e variáveis.

Eles podem servir para calcular, comparar ou alterar o valor de uma variável.

### `Operadores Aritméticos`

São usados para realizar cálculos matemáticos.

- `+` soma
- `-` subtração
- `*` multiplicação
- `/` divisão
- `//` divisão inteira
- `%` resto da divisão
- `**` potência

- Exemplo: `10 + 5` retorna `15`

### `Operadores Relacionais`

São usados para comparar valores.

O resultado sempre será um valor lógico: `True` ou `False`.

- `>` maior que
- `<` menor que
- `>=` maior ou igual
- `<=` menor ou igual
- `==` igual
- `!=` diferente

- Exemplo: `10 > 5` retorna `True`

### `Operadores de Atribuição`

São usados para atualizar o valor de uma variável de forma mais prática.

- `=` recebe um valor
- `+=` soma e atualiza
- `-=` subtrai e atualiza
- `*=` multiplica e atualiza
- `/=` divide e atualiza
- `//=` faz divisão inteira e atualiza
- `%=` pega o resto da divisão e atualiza
- `**=` faz potência e atualiza

- Exemplo: `pontos += 5` é o mesmo que `pontos = pontos + 5`

### `Diferença entre = e ==`

O `=` serve para guardar um valor em uma variável.

- Exemplo: `nome = "Bagha"`

O `==` serve para comparar se dois valores são iguais.

- Exemplo: `nome == "Bagha"` retorna `True`

### `Ordem de Precedência`

Python segue a ordem matemática das operações.

Primeiro resolve potência, depois multiplicação/divisão e por último soma/subtração.

- Exemplo: `2 + 3 * 4` retorna `14`
- Exemplo: `(2 + 3) * 4` retorna `20`