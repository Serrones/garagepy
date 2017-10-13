"""
Crie 10 pastas com o nome "pasta_n" e dentro de cada pasta crie 2 arquivos
'arquivo_x'. Exiba toda estrutura do diretório
"""

import os
import shutil
from pathlib import Path

# create folders
for x in range(1,11):
    os.mkdir(f'pasta_{x}')

# create a list
l = [f for f in os.listdir('.') if f.startswith('pasta')]

# create 2 files in each folder
for el in l:
    Path(f'{el}/arquivo_x.txt').touch()
    Path(f'{el}/arquivo_y.txt').touch()

for i in os.walk('.'):
    print(i)
