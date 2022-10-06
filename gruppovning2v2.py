import random


def fragaantal():  # antal rundor
    while True:
        try:
            antal = int(input("How many questions are you ready for? "))
            if antal > 0:
                return antal
            else:
                print("Please enter an integer which is bigger than 0")
        except ValueError:
            print("Please enter an integer which is bigger than 0")


def fragasvarighetsgrad():  # svårighetsgrad
    while True:
        try:
            svarighetsgrad = int(input("How difficult do you want this test to be (1-3)? "))
            if 0 < svarighetsgrad < 4:
                return svarighetsgrad
            else:
                print("Please enter and integer which is in the range (1-3)")
        except ValueError:
            print("Please enter and integer which is in the range (1-3)")


def rand_tal(svarighetsgrad): # Generera tal enligt svårighetsgrad
    if svarighetsgrad == 1:
        tal1 = random.randrange(1, 10)
        tal2 = random.randrange(1, 10)
        talList = [tal1, tal2]
        return talList
    elif svarighetsgrad == 2:
        tal1 = random.randrange(1, 9) # 10 och 100 för lätt
        tal2 = random.randrange(11, 99)
        talList = [tal1, tal2]
        return talList
    else:
        tal1 = random.randrange(11, 99)
        tal2 = random.randrange(11, 99)
        talList = [tal1, tal2]
        return talList


def rakna(antal, svarighetsgrad):  # testa svaret
    correct = 0
    for i in range(antal):
        userInputCheck = True # För user input check
        talList = rand_tal(svarighetsgrad)
        tal1 = talList[0]
        tal2 = talList[1]
        product = tal1*tal2
       
       # User input check
        while userInputCheck == True:
            try:
                print("What is", tal1, "times", tal2, "?")
                user = int(input())
                userInputCheck = False
            except:
                print("Input needs to be an integer")

        if (test(product, user) == "Incorrect"):
            print("Sorry, the correct answer is", product)
        elif (test(product, user) == "Correct"):
            print("Perfect!")
            correct += 1
            if svarighetsgrad < 3:
                svarighetsgrad += 1
        else:
            print("No.")
    return correct


def test(product, user):
    if user == product:  # rätt-meddelande
        return "Correct"
    else:  # fel-meddelande
        return "Incorrect"


def grade(gradepercentage):
    if gradepercentage == 1:
        return 5
    elif gradepercentage >= 0.8:
        return 4
    elif gradepercentage >= 0.7:
        return 3
    elif gradepercentage >= 0.6:
        return 2
    elif gradepercentage >= 0.5:
        return 1
    else:
        return 0


def main():  # huvudfunktionen, samlar input och kör testet
    correct = 0
    antal = fragaantal()
    svarighetsgrad = fragasvarighetsgrad()
    correct = rakna(antal, svarighetsgrad)
    print("I asked you", antal, "questions and you answered", correct, "of them correctly")
    gradepercentage = correct/antal
    print("This gives you grade", grade(gradepercentage))


main()