import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()


    def play(word):
        word_completion = "_" * len(word)
        guessed = False
        guessed_letter = []
        guessed_word = []
        tries = 6
        print("wanna play some Hangman?")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("please guess a letter or a word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("already guessed the letter", guess)
                elif guess not in word:
                    print:(guess, "is not in the word.")
                    tries -=1
                    guessed_letters.append(guess)
                else:
                    print("osss!,", guess, "is in the word")
                    guessed_letters.append(guess)
                    word_as_list = list (word_completion)
                    indicies = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] =  guess
                    word_completion = "".join(word_as_list)
                    if "_"not in word_completion:
                        guessed = true
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("(spasibo)already guessed this word", guess)
                elif guess != word:
                    print(guess, "is wrong.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = true
                    word_completion = word
            else:
                print("not a valid guess.")
            print(display_hangman(tries))
            print(word_completin)
            print("\n")
        if guessed:
            print("winner by submission,(osss)!")
        else:
            print("it's a tough one to swallow, you ran out of tries. the word was" + word + ".spasibo for playing")






        i\
        def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("wanna roll? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
