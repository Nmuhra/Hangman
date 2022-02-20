from turtle import clear
from art import stages,logo
from words import word_list
import random

word = random.choice(word_list)
length = len(word)

game_over = False
tries = 6
print(logo)

display = []
for _ in range(length):
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f"you have already guessed {guess}.")
    for position in range(length):
        letter = word[position]
        if letter == guess:
            display[position] = letter
  
    if guess not in word:
        print(f"{guess} is not in the Word.")
        tries -= 1
        if tries == 0:
            game_over = True
            print("You lose.")
            print(f"the word was{word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[tries])
