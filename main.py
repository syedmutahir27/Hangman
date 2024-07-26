import os
import sys
import random
import hangman_words
import hangman_art
print(hangman_art.logo)
clear = lambda:os.system('cls')


display = []
chosen_word = random.choice(hangman_words.word_list)
# print(f"psst, the chosen word is {chosen_word}")



#creating blanks
for letter in chosen_word:
    display +="_"

print(f"{''.join(display)}")
end_of_game = False
lives = 10
my_guessed = []
while not end_of_game:
    guess = input("guess the letter : ").lower()
    clear()
    my_guessed.append(guess)
    print(f"your guessed letters till now : {' '.join(map(str,my_guessed))} ")
    

    if guess in display:
        print(f"you already guessed {guess}")
    #check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed the letter {guess} ,that's not in the word.you lose a life")
        if lives == 0:
            end_of_game = True
            print("YOU LOSE")
            print(f"the word was : {chosen_word}")
    print(f"lives left : {lives}")
    print(f"{''.join(display)}")
    if '_' not in display:
        end_of_game = True
        print(("you win"))

    print(hangman_art.stages[lives])

# if __name__ == "__main__":
#     sys.exit