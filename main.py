#Step 5

import random
import hangman_words
import hangman_art

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
exists = False
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
   
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            if display[position] == letter:
              exists = True
            else:
              display[position] = letter
        if exists == True:
          print(f"You've already guessed the letter {letter}.")
          exists = False
    print(hangman_art.stages[lives])

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Sorry, the letter {letter} isn't in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(hangman_art.lose)

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(hangman_art.win)

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
