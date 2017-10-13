"""
Criar um diretório 'aulinha_01', caso ele não exista, e criar um arquivo
chamado 'xpto.txt', e se o arquivo já existir, removeremos e usaremos o novo.
A partir do 'xpto.txt' vamos copiar este arquivo em outros 3 arquivos. ao final,
vamos listar o diretório e fazer uma assertiva de que nesse diretório só
existam 4 arquivos
"""
import os
import os.path
import shutil
from pathlib import Path

# Verify if the file already exists. If not, it's created
if os.path.exists('aulinha_01'):
    print('Diretório já existe')
else:
    os.mkdir('aulinha_01')
    x = os.path.abspath('aulinha_01')
    print('Diretório criado com sucesso!')
    print(x)

# change directory
os.chdir('aulinha_01')

# print path
print(os.getcwd())

# create a file
Path('xpto.txt').touch()

# copy files
for el in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{el}.txt')

# assert the file number
assert len(os.listdir('.')) == 4

arquivos = os.listdir('.')

print(arquivos)
