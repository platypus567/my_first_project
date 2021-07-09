from random import randint
choices = ["Rock", "Paper", "Scissors"]
computer = choices[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, or Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Scissors":
            print("Player Wins! Rock Smashes Scissors")
        if computer == "Paper":
            print("Computer Wins! Paper Covers Rock")
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer Wins! Scissors Cut Paper")
        if computer == "Rock":
            print("Player Wins! Paper Covers Rock")
    elif player == "Scissors":
        if computer == "Paper":
            print("Player Wins! Scissors Cut Paper")
        if computer == "Rock":
            print("Computer Wins! Rock Smashes Scissors")
    else:
        print("Invalid Play")

    player = False
    computer = choices[randint(0,2)]
