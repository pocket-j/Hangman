# Write your code here
import random


def check_lives(life):
    if life == 0:
        print("You are hanged!")
        exit()


def check_accuracy(temp_word, random_word):
    if '_' not in temp_word:
        print(f'You guessed the word {random_word}!')
        print("You survived!")
        exit()


def check_error_input(letter_input, typed_letters, temp_word):
    if letter_input in typed_letters:
        print("You already typed this letter")
    elif len(letter_input) != 1:
        print("You should input a single letter")
    elif not letter_input.islower():
        print("It is not an ASCII lowercase letter")
    else:
        return False
    print()
    print(temp_word)
    return True


def start_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    random_word = random.choice(word_list)
    temp_word = "-" * len(random_word)
    print(temp_word)
    typed_letters = []
    lives = 8
    while True:
        letter = input(f'Input a letter: ')
        if check_error_input(letter, typed_letters, temp_word):
            continue
        if letter in random_word:
            for index in range(len(random_word)):
                if random_word[index] == letter:
                    temp_word = temp_word[:index] + letter + temp_word[index + 1:]
            check_accuracy(temp_word, random_word)
        else:
            lives -= 1
            print("No such letter in the word")
            check_lives(lives)
        typed_letters.append(letter)
        print()
        print(temp_word)


def menu():
    print('Type "play" to play the game, "exit" to quit:')
    user_input = input()
    if user_input == 'exit':
        exit()
    elif user_input == 'play':
        start_game()
        menu()
    else:
        menu()


print("H A N G M A N")
menu()
