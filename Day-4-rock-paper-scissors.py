import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
try:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if user_input >= 3 or user_input <= 0:
        print("You've entered an invalid choice. You lose")
    else:
        print(game_images[user_input])
        computer_choice = random.randint(0, 2)
        print(f"Computer chose:\n {game_images[computer_choice]}")

        if user_input == 0 and computer_choice == 2:
            print("You win")
        elif user_input == 2 and computer_choice == 1:
            print("You win")
        elif user_input == 1 and computer_choice == 0:
            print("You win")
        elif user_input == computer_choice:
            print("It's a draw")
        else:
            print("You lose")
except:
    print("That's not a valid number")
