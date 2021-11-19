"""
Name: Tucker Kilcoyne
lab11.py
"""

from random import randint


def getFile(file_name):
    file = open(file_name, 'r')
    words = []
    for line in file:
        words.append(line.strip())
    return words


def getWord(words):
    secret_word = words[randint(0, len(words))]
    return secret_word


def guessedWord(secret_word, guessed_word, letter, guessed_letters):
    check = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    guessed_letters.append(letter)
    return False


def guessLetters(secret_word, guessed_word, guessed_letters):
    letter = input("Guess a letter: ")
    check = False
    while check == False:
        check = True
        for i in guessed_letters:
            if letter == i:
                print("This letter has already been guessed, try again:")
                letter = input("Guess a letter: ")
                letter.lower()
                check = False
        if (len(letter) != 1) or not (ord(letter) >= 97 and ord(letter) <= 122):
            print("This is an invalid entry, try again.")
            letter = input("Guess a letter: ")
            letter = letter.lower()
            check = False
    if guessedWord(secret_word, guessed_word, letter, guessed_letters):
        return True
    return False


def wordSpell(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    return False


def printBoard(guess_word, turn_count, guessed_letters):
    print("------------------------------------------------")
    print("Guessed word: ", guess_word)
    print()
    print("Turn count:", turn_count)
    print("Guessed letters:", guessed_letters)
    print("------------------------------------------------")


def playGame():
    turn_count = 0
    guessed_letters = []
    secret_word = getWord(getFile("wordlist.txt"))
    guessed_word = ["_"] * len(secret_word)
    printBoard(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not wordSpell(guessed_word, secret_word):
        if guessLetters(secret_word, guessed_word, guessed_letters) == False:
            turn_count += 1
            # printBoard(guessed_word, turn_count, guessed_letters)
        printBoard(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("Game is over! You Lose!")
    elif wordSpell(guessed_word, secret_word):
        print("Congratulations you won the game")


def main():
    playGame()
    pass


main()
