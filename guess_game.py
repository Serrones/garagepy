"""
This is a simple guess number game

"""
import random


secret_number = random.randint(1,20)

print('Im thinking of a number between 1 and 20')

#It will be given 6 chances for the gameplayer guess the secret_number
for i in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break

if guess == secret_number:
    if i == 1:
        print('Good job mate! You guessed my number in just ' + str(i) + ' guess')
    elif i == 6:
        print('Uhaa! You almost lost!! You guessed my number  in ' + str(i) + ' guesses')
    else:
        print('Good job mate! You guessed my number in ' + str(i) + ' guesses')
else:
    print('Nope! The number I was thinking of was: ' + str(secret_number))
