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
    print("0 - Create (IMPORTANT)")
    print("1 - Show groups, members, trainers")
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
    try:
        if userInput == '0':
            clearTerminal()
            print("0 - Create (IMPORTANT)\n")
            input(ctl.create())

        elif userInput == '1':
            clearTerminal()
            print('1 - Show groups, members, trainers\n')
            ctl.show()
            input()
        
        elif userInput == '2':
            clearTerminal()
            print('2 - Assign a trainer to a class\n')
            ctl.assignTrainer()
        
        elif userInput == '3':
            clearTerminal()
            print('3 - Set class fee\n')
            ctl.setClassFee()
            input()

        elif userInput == '4':
            clearTerminal()
            print('4 - Add a member to a class\n')
            print(ctl.addMember())
            input()

        elif userInput == '5':
            clearTerminal()
            print('5 - Remove a member from a class\n')
            ctl.removeMember()
            input()

        elif userInput == '6':
            clearTerminal()
            print('6 - Checkin a member in a class\n')
            ctl.checkinMember()
            input()

        elif userInput == '7':
            clearTerminal()
            print('7 - List enrolled member in a class\n')
            ctl.listMemberInClass()
            input()
        
        elif userInput == '8':
            clearTerminal()
            print('8 - List waitlist of a class\n')
            ctl.listMemberWaitClass()
            input()

        elif userInput == '9':
            clearTerminal()
            print('9 - Display available slots of a class\n')
            ctl.classSlotNumber()
            input()

        elif userInput == '10':
            clearTerminal()
            print('10 - Display number of enrolled members of a class\n')
            ctl.classEnrolledNumber()
            input()
        
        elif userInput == '11':
            clearTerminal()
            print('11 - Display number of waitlist members of a class\n')
            ctl.classWaitNumber()
            input()

        elif userInput == '12':
            clearTerminal()
            print('12 - Display number of attendees of a class\n')
            ctl.classAttendNumber()
            input()

        elif userInput == '13':
            clearTerminal()
            print('13 - Display attendance rate of a class\n')
            ctl.classAttendRate()
            input()

        elif userInput == '14':
            clearTerminal()
            print('14 - Display total payment of a class\n')
            print(ctl.totalPayment())
            input()

        elif userInput == '15':
            clearTerminal()
            print('15 - Display classes a member attends\n')
            ctl.memberClass()
            input()

        elif userInput == '16':
            clearTerminal()
            print('16 - Display classes a trainer teaches\n')
            ctl.trainerClass()
            input()
    except Exception: # catch the error so that you can keep testing rather than terminated
        print(f"An error occured. Press enter to return menu.")
        input()
    
    # Repeat the menu
    clearTerminal()
    displayMenu()
    userInput = input('Please select:')