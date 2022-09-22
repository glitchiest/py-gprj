'''Include package random'''
import random

# Global variables
choices = ["rock", "paper", "scissors"]  # 0 = rock, 1 = paper, 2 = scissor
user_score = 0


def checkResults(user, computer):
    global user_score # Use global variable
    
    if user == "rock":
        # Tie
        if computer == "rock":
            print("It's a TIE!")

        # Win
        elif computer == "scissors":
            print("The computer chose  {}, You chose {}. You WON!".format(computer, user))
            user_score += 1

        # Loss
        else:
            print("The computer chose {}, You chose {}. The computer WON!".format(computer, user))

    elif user == "paper":
        # Win
        if computer == "rock":
            print("The computer chose  {}, You chose {}. You WON!".format(computer, user))
            user_score += 1

        # Loss
        elif computer == "scissors":
            print("The computer chose {}, You chose {}. The computer WON!".format(computer, user))
            
        # Tie
        else:
            print("It's a TIE!")

    else:
        # Loss
        if computer == "rock":
            print("The computer chose {}, You chose {}. The computer WON!".format(computer, user))

        # Tie
        elif computer == "scissors":
            print("It's a TIE!")

        # Win
        else:
            print("The computer chose  {}, You chose {}. You WON!".format( computer, user))
            user_score += 1


def userChoice(choices=[]):
    global user_score # Use global variable
    while True:
        print("\nCurrent score: {}".format(user_score))
        print("\nMake your choice:\n1:Rock\n2:Paper\n3:Scissors")
        user = input()
        if int(user) <= 3 and int(user) >= 0:
            user = str(choices[int(user)-1])
            return user
        else:
            print("Chose 1, 2 or 3")


def computerChoice(choices=[]):
    computer = random.randint(0, 2)
    computer = str(choices[computer])
    return computer


print("*****************\nRock - Paper - Scissors\n*****************\n")
pointsNeeded = int(input("How many points are required to win? "))

# The game starts here
while user_score < pointsNeeded:
    user = userChoice(choices)
    computer = computerChoice(choices)
    checkResults(user, computer)