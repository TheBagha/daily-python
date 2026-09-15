# Dia 4

## Objetivo

- Aprender a tomar decisões usando `if`, `elif` e `else`.
- Entender como condições mudam o caminho de execução do programa.
- Usar operadores relacionais e lógicos dentro de condições.

## Anotações

### `if`

O `if` executa um bloco de código apenas quando a condição é verdadeira.

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

Os espaços no começo das linhas formam a indentação. Ela indica quais linhas pertencem à condição.

### `else`

O `else` é executado quando a condição do `if` é falsa.

```python
idade = 16

if idade >= 18:
    print("Pode entrar.")
else:
    print("Não pode entrar.")
```

### `elif`

O `elif` permite testar uma nova condição quando as anteriores forem falsas. É possível usar vários `elif` no mesmo bloco.

```python
nota = 8

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

Python verifica as condições de cima para baixo e executa somente o primeiro bloco verdadeiro.

### Operadores lógicos

- `and`: todas as condições precisam ser verdadeiras.
- `or`: pelo menos uma condição precisa ser verdadeira.
- `not`: inverte o resultado da condição.

```python
idade = 20
tem_ingresso = True

if idade >= 18 and tem_ingresso:
    print("Entrada liberada.")
```

### Condições dentro de condições

Um `if` também pode aparecer dentro de outro `if`. Isso é chamado de condição aninhada.

```python
usuario = "bagha"
senha_correta = True

if usuario == "bagha":
    if senha_correta:
        print("Login realizado.")
```

## Boas práticas

- Termine a condição com `:`.
- Mantenha a indentação consistente, normalmente com quatro espaços.
- Use `elif` quando as opções forem alternativas entre si.
- Valide entradas quando o usuário puder digitar valores fora do esperado.
