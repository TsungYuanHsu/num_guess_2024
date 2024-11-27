# Guess number

import random

r = random.randint(1, 100)
count = 0

while True:
    guess = int(input('Please guess 1 number (between 1 and 100):'))
    count += 1
    if guess == r:
        print('You are right')
        print('You guess', count, 'times')
        break
    elif guess > r:
        print('It is too high')
        print('You guess', count, 'times')
    else:
        print('It is too low')
        print('You guess', count, 'times')
print('Congratulations! The answer is', r)