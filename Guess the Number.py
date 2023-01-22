import random

random_number = random.randint(1, 100)
while True:
    player_input = int(input("Guess the Number: "))
    if player_input == random_number:
        print("You got it!\nCongratulations!")
        break
    elif player_input < random_number:
        print("The number is greater than yours.")
        continue
    elif player_input > random_number:
        print("The number is smaller than yours.")
        continue
