import random
import hangman_words
def contain_blank(list) :
    for item in list :
        if item == "_" :
            return True
def contain_letter(list,letter) :
    for item in list :
        if item == letter :
            return True
spell = random.choice(hangman_words.word_list)
print(f"Chosen word :{spell}")
spell_list = []
guess_list = []
for i  in range(len(spell)):
    spell_list.append("_")
attempt = 6
while attempt>0 and contain_blank(spell_list) :
    user_letter = input("Guess a Letter :").lower()
    count = 0
    new_letter = contain_letter(guess_list,user_letter)
    guess_list.append(user_letter)
    for letter in spell :
        if user_letter == letter and not new_letter:
            spell_list[count] = letter
            guesed =True
        count += 1
    if not guesed :
        attempt -= 1
    guesed = False    
    print(' '.join(spell_list))
if attempt>0 :
    print("You Won.")
else :
    print("You Lose.")
