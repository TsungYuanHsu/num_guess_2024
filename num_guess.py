# Guess number

import random

low = int(input('Please input min number: '))
high = int(input('Please input max number: '))
r = random.randint(low, high)
print('Please guess number between min and mix number')
count = 0

while True:
    guess = int(input('Please guess 1 number (between min and max):'))
    count += 1
    if guess == r:
        print('You are right')
        print('You guess', count, 'times')
        break
    elif guess > r:
        print('It is too high')
    else:
        print('It is too low')
    print('You guess', count, 'times')
print('Congratulations! The answer is', r)