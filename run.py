from app.groupExercise import GroupExercise
from app.member import Member
from app.trainer import Trainer
import os, platform

groupList = []
memberList = []
trainerList = []


def create():
    userInput = input('Input 1 for creating a class, 2 for member, 3 for trainer.\n')
    if userInput == 1:
        while True:
            className = input('Please type the class name\n')
            maxCapacity = input('Please type the maximum of class capacity. Number only.\n')
            if maxCapacity.isnumeric():
                newClass = GroupExercise(className, maxCapacity)
                global groupList
                groupList.append(newClass)
                return input('Class created! Press enter to continue.')
            else:
                print('Capacity must be number only!\n')
    
    elif userInput == 2:
        while True:
            firstName = input('Please type firstName. Alphabets only\n')
            lastName = input('Please type lastName. Alphabets only\n')
            if firstName.isalpha() and lastName.isalpha():
                newMember = Member(firstName.capitalize(), lastName.capitalize())
                global memberList
                memberList.append(newMember)
                return input('Member created! Press enter to continue.')
            else:
                print('Name must be alphabets only!\n')
    
    elif userInput == 3:
        while True:
            firstName = input('Please type firstName. Alphabets only\n')
            lastName = input('Please type lastName. Alphabets only\n')
            expertise = input('Please type expertise of the trainer. Alphabets only\n')
            if firstName.isalpha() and lastName.isalpha() and expertise.isalpha():
                newTrainer = Trainer(firstName.capitalize(), lastName.capitalize(), expertise.capitalize())
                global trainerList
                trainerList.append(newTrainer)
                return input('Trainer created! Press enter to continue.')
            else:
                print('Name and expertise must be alphabets only!\n')









# Provide a clean terminal for user after every function
def clearTerminal():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

# Function to display the menu
def displayMenu():
    print("\n==== WELCOME TO GYM EXERCISE CLASS MANAGEMENT APP ====\n")
    print("1 - Create")
    print("2 - Assign a trainer to a class")
    print("3 - Set class fee")
    print("4 - Add a member to a class")
    print("5 - Remove a member from a class")
    print("6 - Checkin a member in a class")
    print("7 - List enrolled member in a class")
    print("8 - List waitlist of a class")
    print("9 - Display number of attendees of a class")
    print("10 - Display attendance of a class")
    print("11 - Display total payment of a class")
    print("12 - Display classes a member attends")
    print("13 - Display classes a trainer teaches\n")
    
    print("R - Repeat the menu")
    print("Q - Quit\n")


# App start

clearTerminal()

displayMenu()
userInput = input('Please select:')

while userInput.upper() != 'Q':
    if userInput == '1':
        clearTerminal()
        print("1 - Create")
        creat()



