print("WELCOME TO THE GAME HANGMAN")
import random
stages=[r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#creating a word list for the game
word_list=["computer","internet","google","data","bit","browser","reboot","binary","folder","memory","network","homepage","console","cursor","input","output","icon","update","delete","insert","virus"]
computer_choice=random.choice(word_list)
print(computer_choice)

#creating spaces according to the word chosen by computer
display=[]
for i in range(0,len(computer_choice)):
    display+="_"
print(display)

lives=6

not_end=True
while not_end:
#asking user to guess the letter
    user_input=input("Guess the letter: ").lower()

#filling the blanks if the letter is in computer choice
    for position in range(len(computer_choice)):
        alphabet=computer_choice[position]
        if alphabet==user_input:
            display[position]=alphabet
    print(display)

#if user guess a wrong letter
    if user_input not in computer_choice:
        lives-=1
        print(f"You guessed a wrong letter. YOU LOOSE A LIFE. You've {lives} lives left")

    if lives==0:
        not_end=False
        print("You're out of lives. YOU LOSE")

#if all the blank filled up
    if "_" not in display:
        not_end=False
        print("Good job. YOU WIN")

    print(stages[lives])