#!/usr/bin/env python

"""
This program will help with string manipulation


- Obter string do clipboard

- Manipular string

- Devolver string para o clipboard

"""

import pyperclip

texto = pyperclip.paste()

lines = texto.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

texto = '\n'.join(lines)

pyperclip.copy(texto)
