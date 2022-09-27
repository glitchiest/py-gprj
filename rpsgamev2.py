import random

# Global variables
choices = ["rock", "paper", "scissors"]  # 0 = rock, 1 = paper, 2 = scissor
user_score = 0
computer_score = 0
points_needed_cond = True # condition --> points_needed while loop

# Function which compares the computer's and the user's choice and then declares the winner
def checkResults(user, computer):

    round_status = None # tie, userw, computerw
    if user == "rock":
        # Tie
        if computer == "rock":
            round_status = "tie"
            return round_status
        # Win for user
        elif computer == "scissors":
            round_status = "userw"
            return round_status
        # Loss for user
        else:
            round_status = "computerw"
            return round_status
    elif user == "paper":
        # Win for user
        if computer == "rock":
            round_status = "userw"
            return round_status
        # Loss for user
        elif computer == "scissors":
            round_status = "computerw"
            return round_status
        # Tie
        else:
            round_status = "tie"
            return round_status

    else:
        # Loss for user
        if computer == "rock":
            round_status = "computerw"
            return round_status
        # Tie
        elif computer == "scissors":
            round_status = "tie"
            return round_status

        # Win for user
        else:
            round_status = "userw"
            return round_status


# The users choice function
def userChoice(choices=[]):
    while True:
        try:
            print("\nMake your choice:\n1:Rock\n2:Paper\n3:Scissors")
            user_input = int(input())
            # Check that int is between 1-3
            if user_input <= 3 and user_input > 0:
                # array --> 0 = Rock; 1 = Paper; 2 = Scissors
                user_choice = str(choices[user_input-1])
                return user_choice
            else:
                print("Please enter an integer between 1 and 3")
        # If user_input != type int
        except ValueError:
            print("Please enter an integer between 1 and 3")


# Function which generates the computer's choice
def computerChoice(choices=[]):
    computer = random.randint(0, 2)
    computer = str(choices[computer])
    return computer

def announceRoundWinner(round_status, user, computer):
    global user_score, computer_score  # Use global variables
    if round_status == "userw":
        print("The computer chose {}, You chose {}. You WON!".format(computer, user))
        user_score += 1 # Increase user score
    elif round_status == "computerw":
        print("The computer chose {}, You chose {}. The computer WON!".format(computer, user))
        computer_score += 1 # Increase computer score
    else:
        print("It's a TIE!")

def displayScore():
    global user_score, computer_score  # Use global variables
    print("\nYour score: {}".format(user_score))
    print("The computer's score: {}".format(computer_score))

# Get points_needed from user input
while points_needed_cond == True:
    # Input handling
    try:
        print("***********************\nRock - Paper - Scissors\n***********************\n")
        points_needed = int(input("How many points are required to win? "))
        if points_needed < 1:
            print("Please enter an integer which is atleast 1")
        else:
            points_needed_cond = False

    except ValueError:
        print("Please enter an integer which is atleast 1")


# The game starts here
while user_score < points_needed and computer_score < points_needed:
    displayScore()
    user = userChoice(choices)
    computer = computerChoice(choices)
    round_status = checkResults(user, computer)
    announceRoundWinner(round_status, user, computer)

    # Check who won the game
    if user_score == points_needed or computer_score == points_needed:
        if user_score > computer_score:
            print("\nYour final score:", user_score)
            print("The computer's final score:", computer_score)
            print("You WON the game")
        else:
            print("\nYour final Score:", user_score)
            print("The computer's final score:", computer_score)
            print("You LOST the game")
