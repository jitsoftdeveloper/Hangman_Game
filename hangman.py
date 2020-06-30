import WordList
import random
import time


# Select random word from wordlist
def random_word():
    words = WordList.wordlist
    selected_word = random.choice(words)
    return selected_word.lower()


name = input("Enter your name: ")
print("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)


# Start game function
def startgame():

    user_guessed = []
    wrong_guess = []
    playgame = True
    answer = random_word()
    get_word = list(answer)
    tries = len(get_word)

    for i in range(len(get_word)):
        user_guessed.append('_')

    if playgame:
        while True:
            print('\nYour secret word is: ' + ' '.join(user_guessed))
            print('\nTotal number of guesses left: ', tries)

            if user_guessed == get_word:
                print('Yay! Congrats you won....')
                play_again()

            elif tries == 0:
                print('Too many Guesses! Sorry better luck next time.')
                print("The secret word was:- " + answer)
                play_again()
                break

            letter = input('Guess a letter: ').lower()
            if letter in user_guessed or letter in wrong_guess:
                print("You already guessed this letter, try something else.")
            else:
                if letter in get_word:
                    print("Nice guess!")
                    for k in range(len(get_word)):
                        if letter == get_word[k]:
                            user_guessed[k] = letter.lower()

                else:
                    print("Oops! Try again.")
                    tries -= 1
                    wrong_guess.append(letter)


def play_again():
    # Play again logic for the game
    coninue_game = input('\nDo you want to continue game? (yes/no)')

    if coninue_game == 'y' or coninue_game == 'yes':
        startgame()
    else:
        print('See you next time!')


startgame()
