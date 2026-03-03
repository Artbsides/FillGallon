# FillGallon

Aplicação desenvolvida em [Python 3.12+](https://python.org), focada em encontrar a melhor combinação de garrafas para preencher um galão com o menor desperdício possível.

# Desafio

Dado um conjunto de garrafas d'água com volumes diferentes entre si e um galão de água, o algoritmo escolhe quais garrafas utilizar para encher o galão seguindo as regras abaixo, em ordem de prioridade:

1. O galão deve ser completamente preenchido com o volume das garrafas
2. As garrafas escolhidas devem ser esvaziadas totalmente
3. Quando não for possível esvaziar todas as garrafas escolhidas, deixar a menor sobra possível
4. Utilizar o menor número de garrafas possível

# Exemplos

**Exemplo 1** — combinação exata encontrada:
```
Litros do galão: 7
Litros das garrafas (por vírgula): 1,3,4.5,1.5,3.5

Garrafas: [1.0, 4.5, 1.5], Sobra: 0.0
```

**Exemplo 2** — menor sobra possível:
```
Litros do galão: 5
Litros das garrafas (por vírgula): 1,3,4.5,1.5

Garrafas: [1.0, 4.5], Sobra: 0.5
```

**Exemplo 3** — combinação exata com duas garrafas:
```
Litros do galão: 4.9
Litros das garrafas (por vírgula): 4.5,0.4

Garrafas: [4.5, 0.4], Sobra: 0.0
```

# Instalação

É necessário que o ambiente possua o Python instalado previamente. Não há dependências externas — a aplicação utiliza apenas módulos da biblioteca padrão do Python.

```
Python 3.12+
```

# Inicialização

```
$ python main.py
```

# Melhorias Necessárias

* Suporte a argumentos via linha de comando (ex: `--gallon 5 --bottles 1,3,4.5`)
* Tratamento de entradas inválidas com mensagens mais descritivas
* Implementar testes automatizados

# Principais Tecnologias Utilizadas

* [Python](https://python.org)
* [itertools](https://docs.python.org/3/library/itertools.html)
