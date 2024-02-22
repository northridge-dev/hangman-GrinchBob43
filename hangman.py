# BANNER and HANGMAN_PICS are some ASCII art
# Create your own ASCII art if you desire, but
# ONLY AFTER getting the game logic working.
guessed_words = []
from ascii_art import BANNER, HANGMAN_PICS
from os import system
def clear():
  system("clear")

# uncomment the import statement, below, when
# you're ready to implement a one player version
# of the game.
# `animal_words` is a list of . . . animal words.
# Feel free to add more words or word categories.
# from word_lists import animal_words

"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - If you try to write all the code in `play_hangman`, 
    it's going to be a mess. Instead, break your logic
    into smaller functions that you can call from 
    `play_hangman`.

Run your code from the terminal:
  - make sure you're in the right directory (`projects/hangman`)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: python hangman.py

Tests? No tests for this project. 
"""
def ask4werd():
    secret_word = input("*Input secret word* ")
    clear()
    print(BANNER, HANGMAN_PICS [0])
    disp_word = []
    sw_list = []
    for l in secret_word:
      sw_list.append(l)
      disp_word.append("_")
    print(disp_word)

def ask4letter():
    letter = input("*Guess a letter* ")
    guessed_words.append(letter)
    
def testletter():
    index = 0
    if letter in guessed_words:
        print("*You already guessed that!*")
        ask4letter()
    if letter in sw_list and not guessed_words:
        for l in sw_list:
          if l == letter:
            index = 0
            for l in sw_list:
              
          



# Here's where you can define helper functions


# `play_hangman` is the main function, the function
# that will orchestrate all the helper functions
# you define, above.
def play_hangman():
    
    print(BANNER)
    print(HANGMAN_PICS [0])
    ask4werd()
    ask4letter()

    
    


"""
Don't worry about the code below, and don't change it.

It's just a way to trigger the `play_hangman` function
when you run this file from the command line.
"""
if __name__ == "__main__":
    play_hangman()
