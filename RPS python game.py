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
            print("Player Wins!")
        if computer == "Paper":
            print("Computer Wins!")
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer Wins!")
        if computer == "Rock":
            print("Player Wins!")
    elif player == "Scissors":
        if computer == "Paper":
            print("Player Wins!")
        if computer == "Rock":
            print("Computer Wins!")
    else:
        print("Invalid Play")

    player = False
    computer = choices[randint(0,2)]
