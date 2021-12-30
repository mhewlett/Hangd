import random

wordlist = []

with open('wordlist.txt') as f:
    for line in f:
        wordlist.append(line.rstrip('\n'))
          
answer = 'y'

while answer.lower() == 'y':
    enter = 0
    letter = 0
    number = 0
    hidden_word = random.choice(wordlist)
    token = 0
    correct = []
    wrong = []
    attempts = 10
    attempt = 0
    word = ['?' for word in hidden_word]

    print('The word: ')
    print(word)

    print('Can you guess the word?')
    while attempts >= 1:
        word = []
        attempts -= 1
        attempt += 1
        print()
        guess = input('Guess #' + str(attempt) + '. Guess a letter> ')
        print()
        if guess == '':
          enter += 1
        elif guess in hidden_word:
            if guess not in correct:
                token += 1
            else:
                attempts -= 1
            correct.append(guess)
            attempts += 1
        elif guess not in wrong:
            if guess.isalpha():
                if len(guess) > 1:
                    letter += 1
                else:
                    wrong.append(guess)
            else:
                number += 1
        for i in hidden_word:
            if i == ' ':
                word.append(' ')
            elif i not in correct:
                word.append('?')
            else:
                word.append(i)
        print('The word: ')
        print(word)
        print()
        if '?' not in word:
            print('YOU WIN!')
            print('You guessed the word ' + hidden_word)
            print('Good job! :)')
            break
        elif attempts == 0:
            print(str(attempts) + ' attempts left')
            print('You lost the game :(')
            print('The word was ' + (hidden_word))
            break

        print('Wrong guesses: ')
        print(wrong)
        print()
        print(''.center(25,'*'))

        if guess in hidden_word and not enter:
            if token == 1:
                print('Correct guess'.center(25))
                token -= 1
            else:
                print("You've already guessed '" + guess + "'")
        elif enter or letter or number:
            enter = 0
            print('Invalid input'.center(25))
            letter = 0
            number = 0
        else:
            print('Incorrect guess'.center(25))
        print((str(attempts) + ' attempts left').center(25))
        print(''.center(25,'*'))
    print()
    print('Would you like to play again? Y or N')
    answer = input('> ')
    print()

    if answer.lower() == 'y':
        continue
    else:
        break
