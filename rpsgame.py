'''Include package random'''
import random

# Global variables
choices = ["rock", "paper", "scissors"]  # 0 = rock, 1 = paper, 2 = scissor
user_score = 0
computer_score = 0

# Function which compares the computers and the users choice and then declares the winner
def checkResults(user, computer):
    global user_score, computer_score  # Use global variable

    if user == "rock":
        # Tie
        if computer == "rock":
            print("It's a TIE!")

        # Win
        elif computer == "scissors":
            print("The computer chose {}, You chose {}. You WON!".format(computer, user))
            user_score += 1

        # Loss
        else:
            print("The computer chose {}, You chose {}. The computer WON!".format(computer, user))
            computer_score += 1
    elif user == "paper":
        # Win
        if computer == "rock":
            print("The computer chose {}, You chose {}. You WON!".format(computer, user))
            user_score += 1

        # Loss
        elif computer == "scissors":
            print("The computer chose {}, You chose {}. The computer WON!".format(computer, user))
            computer_score += 1
        # Tie
        else:
            print("It's a TIE!")

    else:
        # Loss
        if computer == "rock":
            print("The computer chose {}, You chose {}. The computer WON!".format(computer, user))
            computer_score += 1
        # Tie
        elif computer == "scissors":
            print("It's a TIE!")

        # Win
        else:
            print("The computer chose  {}, You chose {}. You WON!".format(computer, user))
            user_score += 1


# The users choice function
def userChoice(choices=[]):
    global user_score, computer_score  # Use global variable
    while True:
        try:
            print("\nYour score: {}".format(user_score))
            print("\nThe computer's score: {}".format(computer_score))
            print("\nMake your choice:\n1:Rock\n2:Paper\n3:Scissors")
            user_input = int(input())
            # Check that int is between 1-3
            if user_input <= 3 and user_input > 0:
                # array --> 0 = Rock; 1 = Paper; 2 = Scissors
                user_choice = str(choices[user_input-1])
                return user_choice
            else:
                print("Enter an integer number between 1 and 3")
        # If user_input != type int
        except ValueError:
            print("Enter an integer number between 1 and 3")


# Function which generates the computer's choice
def computerChoice(choices=[]):
    computer = random.randint(0, 2)
    computer = str(choices[computer])
    return computer


# Get points_needed from user input
print("*****************\nRock - Paper - Scissors\n*****************\n")
points_needed = int(input("How many points are required to win? "))


# The game starts here
while user_score < points_needed and computer_score < points_needed:
    user = userChoice(choices)
    computer = computerChoice(choices)
    checkResults(user, computer)
    if user_score == points_needed or computer_score == points_needed:
        if user_score > computer_score:
            print("\nYour final score:", user_score)
            print("The computer's final score:", computer_score)
            print("You WON the game")
        else:
            print("\nYour final Score:", user_score)
            print("The computer's final score:", computer_score)
            print("You LOST the game")
