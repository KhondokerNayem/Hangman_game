import random
print("Welcome to the world of word. Here you have to guess the right word. Start you'r guessing. Do within your lifes. Best of luck!")
word_list = ["aardvark", "baboon", "camel", "dog", "elephant", "frog", "giraffe", "hippopotamus", "iguana", "jaguar", 
             "kangaroo", "lion", "monkey", "narwhal", "octopus", "penguin", "quail", 
             "rabbit", "snake", "tiger", "umbrella", "vulture", "wolf", "xenopus", 
             "yak", "zebra", "alligator", "buffalo", "cat", "deer", "eagle", "falcon", 
             "goat", "horse", "insect", "koala", "leopard", "moose", "newt", "ostrich", 
             "parrot", "quokka", "raccoon", "seal", "toucan", "urchin", "viper", 
             "whale", "xerus", "yak", "zebu"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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
=========
''', '''
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

chosen_word = random.choice(word_list)
blank = []
for flag in chosen_word:
    blank.append("-")
life = 6
while True:
    # print(f"You have {life} life!")
    print(stages[life])   
    update = 0
    guess = input("Guess a letter: ").lower()
    number = 0
    for letter in chosen_word:
        if letter == guess:
            blank[number] = letter 
            update += 1
        # print(update)
        number += 1
    output = ""
    for i in blank:   
        output += i  
    print(output) 
    # print(f"Life : {life}")
    if chosen_word == output:
        print("You won! Congrats!")
        break
    # print(f"Update : {update}")
    if update == 0:
        life -= 1
    if life == 0:
        print("You lose! Try for next")
        break
print(stages[0])
print(f"The word is : {chosen_word}")
print("The End")