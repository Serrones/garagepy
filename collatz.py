"""
Crie uma função chamada collatz() que tenha um parâmetro de nome number. Se
number for par, collatz() deverá exibir number // 2 e retornar esse valor. Se
number for ímpar, collatz() deverá exibir e retornar 3 * number + 1.
Em seguida crie um programa em que o usuário passe um número qualquer e fique
chamando collatz até que o resultado seja 1.
"""

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = (3 * number) + 1
            print(number)

print('Hello mate! Please type any number:\n')
try:
    number = int(input())
except ValueError:
    print("Hey mate! You didn't type a real number. Try it again!")
    number = int(input())

collatz(number)
