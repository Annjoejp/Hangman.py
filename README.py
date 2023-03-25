# Hangman.py
import random

# list of possible words
words = ['python', 'computer', 'science', 'programming', 'data']

# function to select a random word
def select_word(words):
    return random.choice(words)

# function to play the game
def play_hangman(word):
    # initialize the guessed word with underscores
    guessed_word = ['_'] * len(word)
    # keep track of guessed letters
    guessed_letters = []
    # number of incorrect guesses
    incorrect_guesses = 0
    # maximum number of incorrect guesses allowed
    max_incorrect_guesses = 6
    
    # loop until the word is guessed or the player runs out of guesses
    while '_' in guessed_word and incorrect_guesses < max_incorrect_guesses:
        print(' '.join(guessed_word))
        print(f'Guessed letters: {" ".join(guessed_letters)}')
        letter = input('Guess a letter: ').lower()
        
        # check if the letter has already been guessed
        if letter in guessed_letters:
            print(f'You already guessed "{letter}"')
            continue
        
        # add the letter to the guessed letters list
        guessed_letters.append(letter)
        
        # check if the letter is in the word
        if letter in word:
            # update the guessed word
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word[i] = letter
        else:
            # incorrect guess
            print(f'"{letter}" is not in the word')
            incorrect_guesses += 1
            
    # check if the player won or lost
    if '_' not in guessed_word:
        print(f'Congratulations, you guessed the word "{word}"')
    else:
        print(f'Sorry, you ran out of guesses. The word was "{word}"')
        
# main function to run the game
def main():
    word = select_word(words)
    play_hangman(word)
    
# run the game
if __name__ == '__main__':
    main()
