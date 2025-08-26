# Hangman Game 

import random
def hangman():
    words_list = ["Strawberry","Orange","Grape","Apple","Pear","Mango","Lychee","Kiwi","Cherry"]
    word = random.choice(words_list).lower()
    tries = 9
    guess_letter = ''
    entries = "abcdefghijklmnopqrstuvwxyz"
    while tries >0:
        main_word = ""
        for letter in word:
            if letter in guess_letter:
                main_word = main_word + letter
            else:
                main_word = main_word + '_ '
        if main_word.replace(" ", "") == word:
            print("You Won!.Your word was:",word)
                
            break
        print("Guess the word", main_word)
        guess = input("Enter a letter: ").lower()
        if guess in entries and len(guess) == 1:
            if guess in guess_letter:
              print(" You already guessed that letter! Now Try something else.")
              continue
            else:
              guess_letter = guess_letter + guess
        else:
            print("Enter Valid char")
            guess = input().lower()
        if guess not in word:
            tries =tries - 1
            if tries == 8:
                print("8 tries are left.!!")
                print("--------------------")
            if tries == 7:
                print("7 tries are left.!!")
                print("--------------------")
                print("            |     ")
            if tries == 6:
                print("6 tries are left.!!")
                print("--------------------")
                print("          __|        ")
            if tries == 5:
                print("5 tries are left.!!")
                print("--------------------")
                print("         O__|       ")
            if tries == 4:
                print("4 tries are left.!!")
                print("--------------------")
                print("         O__|        ")
                print("         |         ")
            if tries == 3:
                print("3 tries are left.!!")
                print("--------------------")
                print("         O__|         ")
                print("        /|         ")
            if tries == 2:
                print("2 triess are left.!!")
                print("--------------------")
                print("         O__|       ")
                print("        /|\         ")
            if tries == 1:
                print("1 tries are left.!!")
                print("--------------------")
                print("         O__|     ")
                print("        /|\         ")
                print("        /         ")
            if tries == 0:
                print("0 tries are left.!!")
                print("--------------------")
                print("         O__|     ")
                print("        /|\         ")
                print("        / \        ")
                print("You Failed")
                print("That was brutal. Wanna try again?? Your word was:",word)
                break


     

name = input("Enter the player name:")
print(f"Welcome {name}. This is Hangman")
print("Guess the number in less than 9 attempts")
hangman()