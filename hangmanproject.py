"""
Project #2: Hangman
7 x 20
  __________________ 0
 _|_               | 1
| _ |              | 2
  |                | 3
/ | \              | 4
  |                | 5
/   \              | 6
"""


import random
import time
import os
import sys

words_list = [
    "apple",
    "banana",
    "carrot",
    "double",
    "elephant",
    "frolic",
    "generator",
    "hybrid",
    "igloo",
    "justify",
    "kangaroo",
    "liquid",
    "monster",
    "nothing",
    "octopus",
    "platypus"
    "query",
    "rugged",
    "styles",
    "typical",
    "unify",
    "validate",
    "withdraw",
    "xenon",
    "yellow",
    "zephyr"
]


def draw_hangman(face=False, neck=False, body=False, left_hand=False, right_hand=False, left_leg=False, right_leg=False):
    for row in range(10):
        if row == 0:
            for column in range(20):
                if column >= 3:
                    if column == 19:
                        print("_")
                    else:
                        print("_", end="")
                else:
                    print(" ", end="")

        # face
        elif face == True and row == 1:
            for column in range(20):
                if column == 0:
                    print(" ", end="")
                elif column == 1:
                    print("_", end="")
                elif column == 2:
                    print("|", end="")
                elif column == 3:
                    print("_", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        elif face == True and row == 2:
            for column in range(20):
                if column == 0 or column == 4:
                    print("|", end="")
                elif column == 1 or column == 3:
                    print(" ", end="")
                elif column == 2:
                    print("_", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        # neck
        elif neck == True and row == 3:
            for column in range(20):
                if column == 2:
                    print("|", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        # left hand
        elif left_hand == True and row == 4:
            for column in range(20):
                if column == 0:
                    print("/", end="")
                elif column == 1:
                    print(" ", end="")
                elif column == 2:
                    print("|", end="")
                elif column == 3:
                    print(" ", end="")
                elif right_hand == True and column == 4:
                    print("\\", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        # body
        elif body == True and row == 5:
            for column in range(20):
                if column == 2:
                    print("|", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        # left leg
        elif left_leg and row == 6:
            for column in range(20):
                if column == 0:
                    print("/", end="")
                elif column == 1:
                    print(" ", end="")
                elif column == 3:
                    print(" ", end="")
                # right leg
                elif right_leg and column == 4:
                    print("\\", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        elif row == 9:
            for column in range(20):
                if column <= 10:
                    print(" ", end="")
                elif column == 19:
                    print("-")
                else:
                    print("-", end="")
        else:
            for column in range(20):
                if column == 19:
                    print("|")
                else:
                    print(" ", end="")




def welcome():
    welcome_text = "Let's play Hangman."
    print(welcome_text)



def computer_pick():
    word = random.choice(words_list)
    return word.lower()



def ask_phrase(repeat_text=None):
    question = repeat_text if repeat_text is not None else "Type your secret word.\n"
    word = input(question)
    if type(word) == str and len(word) >= 3:
        return word.lower()
    else:
        return ask_phrase("Your word must have at least 3 letters. Please choose another word.\n")



def write_guessed_letters(guessed_letters):
    print("Word: ", end="")
    for letter in guessed_letters:
        print(letter, end="  ")
    print("\n")



def guess_check(letter, phrase_letters):
    guess = False
    if letter in phrase_letters:
        guess = True
    return guess


def fill_spaces(letter, phrase_letters, guessed_letters):
    indices = [i for i, el in enumerate(phrase_letters) if el == letter]
    for index in indices:
        guessed_letters[index] = letter
    return guessed_letters



def guess_letter(repeat_question=None):
    question = repeat_question if repeat_question is not None else "What's your guess?\n"
    word = input(question)
    if type(word) == str and len(word) == 1:
        return word.lower()
    else:
        return guess_letter("Hey, one letter at a time! Type again.\n")



def show_incorrect(incorrect):
    print("Incorrect: ", end="")
    for i in incorrect:
        print(i, end=",")
    print("\n")


def incorrect_guess(committed_mistakes):
    if committed_mistakes == 0:
        draw_hangman(False, False, False, False, False, False, False)
    if committed_mistakes == 1:
        draw_hangman(True, False, False, False, False, False, False)
    if committed_mistakes == 2:
        draw_hangman(True, True, False, False, False, False, False)
    if committed_mistakes == 3:
        draw_hangman(True, True, True, False, False, False, False)
    if committed_mistakes == 4:
        draw_hangman(True, True, True, True, False, False, False)
    if committed_mistakes == 5:
        draw_hangman(True, True, True, True, True, False, False)
    if committed_mistakes == 6:
        draw_hangman(True, True, True, True, True, True, False)
    if committed_mistakes == 7:
        draw_hangman(True, True, True, True, True, True, True)



def how_many_players():
    choice = "Which do you choose?\n\n"
    option = "1) One Player Mode\n2) Two Player Mode\n\n"
    game_type = input(choice + option)
    if type(game_type) == str and game_type == "1" or game_type == "2":
        return int(game_type)
    else:
        how_many_players()




def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


# clear screen
def clear_screen():
    platform = get_platform()
    if platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def start_hangman():
    welcome()

    game_type = how_many_players()


    if game_type == 1:
        phrase = computer_pick()

    else:
        phrase = ask_phrase()

    phrase_letters = [x for x in phrase]
    guessed_letters = ["__" in phrase_letters]
    committed_mistakes = 0
    already_guessed_letters = []
    incorrect_letters = []

    # hide the secret word, clear the screen.
    # print(chr(27) + "[2J")
    clear_screen()
    no_win = True


    while committed_mistakes < 7 and no_win:


        incorrect_guess(committed_mistakes)


        write_guessed_letters(guessed_letters)

        if len(incorrect_letters) > 0:
            show_incorrect(incorrect_letters)


        guessed_letter = guess_letter()


        if guessed_letter in already_guessed_letters:
            print("You have already guessed " + guessed_letter + "." + "Please choose a different letter.")
            time.sleep(1)
            clear_screen()
            continue
        else:
            already_guessed_letters.append(guessed_letter)


        guessed = guess_check(guessed_letter, phrase_letters)

        if guessed:
            guessed_letters = fill_spaces(guessed_letter, phrase_letters, guessed_letters)
            print("Good guess. Keep going...")

            if guessed_letters == phrase_letters:
                no_win = False


        else:
            committed_mistakes += 1
            incorrect_letters.append(guessed_letter)
            print("Sorry, that letter was incorrect.")

        time.sleep(1)
        clear_screen()

    if not no_win:
        write_guessed_letters(guessed_letters)
        print("Congratulations. You won!")

    if committed_mistakes == 7:
        incorrect_guess(committed_mistakes)
        print("Sorry, you lost.")
        print('The word was', phrase)



start_hangman()