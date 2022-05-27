import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    print("computer: ",computer)
    print("player: ",player)
    if player == computer:
        print("tie!")
    elif player == "rock":
        if computer == "scissors":
            print("congrats, you won")
        elif computer == "paper":
            print("you lose, try again")
    elif player == "paper":
        if computer == "rock":
            print("congrats, you won")
        elif computer == "scissors":
            print("you lose, try again")
    elif player == "scissors":
        if computer == "paper":
            print("congrats, you won")
        elif computer == "rock":
            print("you lose, try again")
    else:
        print("hold up, wait a min, smth aint right")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("cya")
