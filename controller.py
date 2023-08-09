from model.groupExercise import GroupExercise
from model.member import Member
from model.trainer import Trainer

groupList = []
memberList = []
trainerList = []

# Auto create all objects
def create():
    userInput = input('Press enter to create 2 GroupExercise objects, 5 Member objects and 2 Trainer objects.\n')
    global groupList
    global memberList
    global trainerList
    
    groupList = [GroupExercise('Swimming', 5), GroupExercise('Running', 5)]
    memberList = [Member('Haochen', 'Zhu'), Member('Lu', 'Lu'), Member('Yang', 'Yang'), Member('Silver', 'Wang'), Member('Leo', 'Zhao')]
    trainerList = [Trainer('Bill','Gates', 'Swimming'), Trainer('Elon','Musk', 'Running')]

    return ('All objects created!')

# Checking all objects
def show():
    if groupList != [] and memberList != [] and trainerList != []:
        input('Press enter to show groups')
        for index, group in enumerate(groupList):
            print(index, group)
        
        input('\nPress enter to show members')
        for index, member in enumerate(memberList):
            print(index, member)

        input('\nPress enter to show trainers')
        for index, t in enumerate(trainerList):
            print(index, t)

        input('\nPress enter to return')
    else:
        input('\nPlease create objects first!')

# Choose a class and assign a trainer.
def assignTrainer():
    if groupList != [] and trainerList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            for index,t in enumerate(trainerList):
                print(f'{index} {t.firstName} {t.lastName}')
            trainerInput = int(input('Please choose the trainer. Number only.\n'))

            #validate object 
            if (0 <= groupInput < len(groupList)) and (0 <= trainerInput < len(trainerList)):
                return groupList[groupInput].assignTrainer(trainerList[trainerInput])
            else:
                print('Incorrect index!')
            
# set the class fee as int                
def setClassFee():
    if groupList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')
            feeInput = input('Please input the fee per person. Number only.\n')

            #validate group and fee
            if (0 <= groupInput < len(groupList)) and feeInput.isnumeric():
                return groupList[groupInput].setFee(int(feeInput))
            else:
                print('Incorrect index or fee!')

    else:
        return input('No class has been created.\n')
    
# Add member to a class
def addMember():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            for index,t in enumerate(memberList):
                print(f'{index} {t.firstName} {t.lastName}')
            memberInput = int(input('Please choose the member. Number only.\n'))

            #validate object 
            if (0 <= groupInput < len(groupList)) and (0 <= memberInput < len(memberList)):
                result = groupList[groupInput].enrol(memberList[memberInput])
                #add groupObject to memberClass if success
                if result[1] == 1:
                    memberList[memberInput].enrol(groupList[groupInput])
                input(result[0])

            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

def removeMember():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # show members
            if (0 <= groupInput < len(groupList)):
                for index,member in enumerate(groupList[groupInput].memberAll):
                    print(index, member)
                memberInput = int(input('Please choose the member to remove. Number only.\n'))

                if (0 <= memberInput < len(groupList[groupInput].memberAll)):
                    result = groupList[groupInput].removeMember(member)

                    if result == 1:
                        member.cancelEnrol(groupList[groupInput])
                    
                    input(result[0])
                else:
                    input('Incorrect index!')
            else:
                input('Incorrect index!')

                
