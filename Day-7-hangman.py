import random
import hangman_art as ha
import hangman_word as hw

print(ha.logo)
#TODO-1: - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hw.word_list)
word_len = len(chosen_word)

#TODO-2: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#TODO-3: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
display = display + ['_'] * word_len

#TODO-4 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
#Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for index in range(word_len):
    letter = chosen_word[index]
    if letter == guess:
      display[index] = letter
  #TODO-5: - If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose.")
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")
  #TODO-6: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(ha.stages[lives])