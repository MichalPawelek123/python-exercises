"""
Hangman game with 6 lives without graphical representation,
Words used: 
http://norvig.com/ngrams/sowpods.txt 
or create your own file where each word is in the new line
"""

import random

def pick_a_word(file_name): 
    with open(f'{file_name}', 'r') as f: 
        lines = f.readlines()
        number = random.randint(0, len(lines) -1)
        return lines[number].strip()

# check if any letter from the list of letters that user used is in the hidden word
def reveal_letters(word, guessed_letters): 
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters: 
            hidden_word += letter
        else:
            hidden_word += " _ "

    return hidden_word

     
def main(): 
    hidden_word = pick_a_word('list_of_words.txt').lower()
    guessed_letters = []
    lives = 6

    WORD = reveal_letters(hidden_word, guessed_letters)

    while True: 
        # round info, show current state of word, lives left and already guessed letters
        print("\n\n\n\n\n", WORD)
        print(f"You have {lives} lives left")
        if len(guessed_letters) != 0:
            print(f'Those are the letters you already tried: {guessed_letters}')

        # conditions to end the game
        if WORD == hidden_word: 
            print("Congratulations, you guessed the right word: ", hidden_word)
            break
        elif lives == 0: 
            print("You got hanged :( ", f"The hidden word was: {hidden_word}", )

            break

        user_guess = ""
        while len(user_guess) != 1:
            user_guess = input("Guess a letter(or a whole hidden word): ").lower()

            if user_guess not in hidden_word:
                lives -= 1
            if user_guess == hidden_word: 
                print("Congratulations, you guessed the right word: ", hidden_word)
                exit()
            if len(user_guess) != 1: 
                print("One letter is enough")

        guessed_letters.append(user_guess)
        WORD = reveal_letters(hidden_word, guessed_letters)


main()