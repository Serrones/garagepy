"""
Crie 10 arquivos com o nome "live_n.txt" onde n é o número do arquivo e
delete os arquivos em que o valor é menor ou igual a 5. Quando isso estiver
feito, renomeie os arquivos de 6 a 10 para 1 a 5.
"""

import os
import shutil
from pathlib import Path

# create files
for i in range(1, 11):
    Path(f'live_{i}.txt').touch()

# create a file list
l = [f for f in os.listdir('.') if f.startswith('live')]

# remove files less than 6
for f in l:
    if int(f.partition('_')[2][0]) <= 5:
        os.remove(f)

# create a new list and rename files
x = [f for f in os.listdir('.') if f.startswith('live')]
num = 1
for arq in x:
    shutil.move(arq, f'live_{num}.txt')
    num +=1
