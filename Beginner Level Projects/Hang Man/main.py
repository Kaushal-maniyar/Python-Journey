import random
import hangman_words
from check import *


spell = random.choice(hangman_words.word_list)
spell_list = []
guess_list = []
for i in range(len(spell)):
    spell_list.append("_")
attempt = 6
while attempt > 0 and contain_blank(spell_list):
    guessed = False
    user_letter = input("Guess a Letter :").lower()
    count = 0
    new_letter = contain_letter(guess_list, user_letter)
    guess_list.append(user_letter)
    for letter in spell:
        if user_letter == letter and not new_letter:
            spell_list[count] = letter
            guessed = True
        count += 1
    if not guessed:
        attempt -= 1
    print(' '.join(spell_list))
    print(f"Your attempt left: {attempt}")
if attempt > 0:
    print("You Won.")
else:
    print("You Lose.")
