import os, platform
import controller as ctl

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
    print("9 - Display available slots of a class")
    print("10 - Display number of enrolled members of a class")
    print("11 - Display number of waitlist members of a class")
    print("12 - Display number of attendees of a class")
    print("13 - Display attendance rate of a class")
    print("14 - Display total payment of a class")
    print("15 - Display classes a member attends")
    print("16 - Display classes a trainer teaches\n")
    
    print("R - Repeat the menu")
    print("Q - Quit\n")


# App start

clearTerminal()
displayMenu()
userInput = input('Please select:')

while userInput.upper() != 'Q':
    if userInput == '1':
        clearTerminal()
        print("1 - Create\n")
        ctl.create()
    
    elif userInput == '2':
        clearTerminal()
        print('2 - Assign a trainer to a class\n')
        print(ctl.assignTrainer())
        input()
    
    elif userInput == '3':
        clearTerminal()
        print('3 - Set class fee\n')
        ctl.setClassFee()

    elif userInput == '4':
        clearTerminal()
        print('4 - Add a member to a class\n')
        ctl.addMember()

    elif userInput == '5':
        clearTerminal()
        print('5 - Remove a member from a class\n')
        ctl.removeMember()

    elif userInput == '6':
        clearTerminal()
        print('6 - Checkin a member in a class\n')
        ctl.checkinMember()

    elif userInput == '7':
        clearTerminal()
        print('7 - List enrolled member in a class\n')
        ctl.listMemberInClass()
    
    elif userInput == '8':
        clearTerminal()
        print('8 - List waitlist of a class\n')
        ctl.listMemberWaitClass()

    elif userInput == '9':
        clearTerminal()
        print('9 - Display available slots of a class\n')
        ctl.classSlotNumber()

    elif userInput == '10':
        clearTerminal()
        print('10 - Display number of enrolled members of a class\n')
        ctl.classEnrolledNumber()
    
    elif userInput == '11':
        clearTerminal()
        print('11 - Display number of waitlist members of a class\n')
        ctl.classWaitNumber()

    elif userInput == '12':
        clearTerminal()
        print('12 - Display number of attendees of a class\n')
        ctl.classAttendNumber()

    elif userInput == '13':
        clearTerminal()
        print('13 - Display attendance rate of a class\n')
        ctl.classAttendRate()

    elif userInput == '14':
        clearTerminal()
        print('14 - Display total payment of a class\n')
        ctl.totalPayment()

    elif userInput == '15':
        clearTerminal()
        print('15 - Display classes a member attends\n')
        ctl.memberClass()

    elif userInput == '16':
        clearTerminal()
        print('16 - Display classes a trainer teaches\n')
        ctl.trainerClass()
    
    # Repeat the menu
    clearTerminal()
    displayMenu()
    userInput = input('Please select:')