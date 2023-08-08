from model.groupExercise import GroupExercise
from model.member import Member
from model.trainer import Trainer

groupList = []
memberList = []
trainerList = []


def create():
    userInput = input('Input 1 for creating a class, 2 for member, 3 for trainer.\n')
    if userInput == '1':
        while True:
            className = input('Please type the class name\n')
            maxCapacity = input('Please type the maximum of class capacity. Number only.\n')
            if maxCapacity.isnumeric():
                newClass = GroupExercise(className, int(maxCapacity))
                global groupList
                groupList.append(newClass)
                return input('Class created! Press enter to continue.')
            else:
                print('Capacity must be number only!\n')
    
    elif userInput == '2':
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
    
    elif userInput == '3':
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
            
                




            

    
    else:
        return input('Either no class or trainer has been created.\n')