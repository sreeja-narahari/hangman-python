import random
import hangman_words
import hangman_art

print(hangman_art.logo)


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
    
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
#letter already guessed
    if guess in display:
        print(f"You already guessed {guess}")
        
#replace blanks
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter    
            
#Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You loose a life.")
        lives -= 1
        print(lives) 
#No more lives 
    if lives == 0:
        end_of_game = True
        print("You lose.")

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

#respective images
    print(hangman_art.stages[lives])