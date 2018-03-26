"""
Crie uma função que aceite um valor de lista como argumento e retorne uma string
com todos os itens separados por uma vírgula e um espaço, com 'e' inserido
antesdo último ítem.

"""


lista = []

while True:
    print('Favor digitar algum ítem para a lista: ')
    print('Caso queira encerrar a lista, basta clicar em "enter"')
    item = input()
    if item == '':
        break
    lista.append(item)
if lista == []:
    print('A lista ainda está vazia!')
else:
    lista.sort()

def embeleza(texto):
    frase = []
    for palavra in range(len(texto)):
        if texto[palavra] == texto[-2]:
            frase.append(texto[palavra])
        elif texto[palavra] == texto[-1]:
            frase.append(' e ')
            frase.append(texto[palavra])
            frase.append('!!')
        else:
            frase.append(texto[palavra])
            frase.append(', ')
    corpo_texto = 'A sua lista contém ' + ''.join(frase)
    print(corpo_texto)

embeleza(lista)
