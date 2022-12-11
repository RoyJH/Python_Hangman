import random
from hangman_art import stages, logo, win, lose
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
exists = False
print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
   
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            if display[position] == letter:
              exists = True
            else:
              display[position] = letter
        
        if exists == True:
            print(f"You've already guessed the letter {letter}.")
            exists = False

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"Sorry, the letter {letter} isn't in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(lose)
    print(stages[lives])
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(win)
