import random


computer_points = 0
My_points = 0
if My_points or computer_points == 10:
    print("game is over")
else:

    computer_points = 0
    My_points = 0
    while True:
        options = ["rock","paper","scissors"]
        yourchoice = input("choose rock paper or scissors\n")
        computer_side = random.choice(options)
        print(f"You chose {yourchoice} and the computer chose {computer_side}")
        computer_side = random.choice(options)
        if yourchoice == computer_side:
            print("its a tie!")
            computer_points =+ 1
            My_points =+ 1
        elif  computer_side == "rock":
            if yourchoice == "paper":
                print("you won this round")
                My_points =+ 1
            if yourchoice == "scissors":
                print("you lost! :(")
                computer_points =+ 1
        elif computer_side == "paper":
            if yourchoice == "scissors":
                print("you won this round")
                My_points =+ 1
            if computer_side == "rock":
                print("you lost! :(")
        elif  computer_side == "scissors":
            if yourchoice == "rock":
                print("you won this round")
                My_points =+ 1
            if yourchoice == "paper":
                print("you lost :(")
                computer_points =+ 1
        print(f"Computer points:{computer_points}")
        print(f"My points:{My_points}")
