import random


user_name = input('Enter your name: ')
answer = random.randint(1,100)
trial = 3

# for debugging.
print(answer)

while trial>0:
    guess = int(input('Welcome, {}. Guess the number! : '.format(user_name)))

    if guess==answer:
        print('Correct!!')
        break
    else:
        trial -= 1
        if trial > 0:
            msg = 'Wrong!!! Try again. (You have {} more chance.)'.format(trial)
        else:
            msg = 'You lose!!!!!!!!'
        print(msg)
