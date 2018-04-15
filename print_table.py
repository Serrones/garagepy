#!/usr/bin/env python
"""
Crie uma função que receba lista de listas de strings e a exiba em uma bela
tabela bem organizada, com cada coluna justificada à direita
"""

import pprint


listagem = [
            ['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']
            ]


def print_table(lista):
    # Descobrir o elemento com maior número de strings de todas as listas
    tamanho_col = 0
    for linha in range(len(lista[0])):
        for coluna in range(len(lista)):
            if len(lista[coluna][linha]) > tamanho_col:
                tamanho_col = len(lista[coluna][linha])

    # Criação de linhas. Cada linha com um elemento de cada lista
    for linha in range(len(lista[0])):
        nova_linha = [ (lista[coluna][linha]).rjust(tamanho_col)
                        for coluna in range(len(lista))
                    ]
        print(''.join(nova_linha))

print_table(listagem)
