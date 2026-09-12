# Dia 2

## Objetivo

- Aprofundamento com variáveis e tipos primitivos no Python.
- Aprender a utilizar f-strings ou format.

## Anotações

### `Tipos primitivos`
    
    Variáveis além de armazenar informações também podem receber diferentes tipos.

### `Tipo String`

    Guarda caracteres ou frases entre aspas simples ou duplas. Pode ser declarada utilizando a classe str().

    - Exemplo: "Eai" ou 'Bagha'

### `Tipo Integer`
    
    Guarda números inteiros, sejam positivos ou negativos.
    Pode ser declarada utilizando a classe int().

    - Exemplo: -1 ou 17

### `Tipo Float`

    Guarda números com casas decimais(negativos e positivos).
    Pode ser declarada utilizando a classe float().

    - Exemplo: -87.12 ou 12.5

### `Tipo Bool`

    Guarda um valor lógico verdadeiro (True) ou falso (False).

### `Função type()`

    Usado para descobrir o tipo de dado de uma variável.

    - Exemplo: type(10) retorna <class 'int'>.

## `Formatação de String`

### `F-Strings`

    Para utilizar, basta inserir f ou F antes das aspas da string e colocar as variáveis ou expressões diretamente entre chaves {}.

    - Exemplo: f"Olá, {nome}!"

### `.format()`

    O método .format() é uma alternativa mais antiga, mas ainda encontrada em códigos legados e antigos.

    Exemplo: "Olá, {}!".format(nome)
