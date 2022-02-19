import random
from words import word_list

txt = random.choice(word_list)
length = str(len(txt))
print("the word is "+length+" letters")
guess = input("guess the word\n ")

if guess == txt :
  print("that's right you win!")

else :
    print("wrong guess, you lose!")
