# Guess number

import random

r = random.randint(1, 100)

while True:
    guess = int(input('Please guess 1 number (between 1 and 100):'))
    if guess == r:
        print('You are right')
        break
    elif guess > r:
        print('It is too high')
    else:
        print('It is too low')
print('Congratulations! The answer is', r)