import random
from art import logo
 
def easy_mode():
    actual_number = random.randint(1,100)
    for attempt in range(10,0,-1):
        guess_number = int(input(f"you have {attempt} attempts remaining to guess the number.\nmake a guess: "))
        if guess_number < actual_number:
            print('too low.')
            if attempt != 1:
                print('guess again.')
        elif guess_number > actual_number:
            print('too low.')
            if attempt != 1:
                print('guess again.')
        else:
            return f'you got it! the answer was {actual_number}.'
    return 'you\'ve run out of guesses. you lose.'

def hard_mode():
    actual_number = random.randint(1,100)
    for attempt in range(5,0,-1):
        guess_number = int(input(f"you have {attempt} attempts remaining to guess the number.\nmake a guess: "))
        if guess_number < actual_number:
            print('too low.')
            if attempt != 1:
                print('guess again.')
        elif guess_number > actual_number:
            print('too high.')
            if attempt != 1:
                print('guess again.')
        else:
            return f'you got it! the answer was {actual_number}.'
    return 'you\'ve run out of guesses. you lose.'


print(logo)
q = input('welcome to the number guessing game!\ni\'m thinking of a number between 1 and 100.\n\
choose a difficulty. type "easy" or "hard": ')
if q == 'easy':
    print(easy_mode())
elif q == 'hard':
    print(hard_mode())

    


    



