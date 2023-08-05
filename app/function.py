def hello():
    return print('hello')

class groupExercise:
    def __init__(self, className, trainer, maxCapacity, memberAll, memberWaitlist, feeAmount, memberCheckin):
        self.className = className
        self.trainer = trainer
        self.maxCapacity = maxCapacity
        self.memberAll = memberAll
        self.memberWaitlist = memberWaitlist
        self.feeAmount = feeAmount
        self.memberCheckin = memberCheckin

    def enrol(member):
        pass

class member:
    def __init__(self, firstName, lastName, idNumber, enrolClassList):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.enrolClassList = enrolClassList
    
    def enrol(groupExercise):
        pass

    def cancelEnrol(groupExercise):
        pass

    def EnrolClassDisplay():
        if member.enrolClassList != []:
        
            print(member.firstName + " " + member.lastName + 'has enrolled the following classes.' )
        
            for i in member.enrolClassList:
                print(i)

class trainer:
    def __init__(self, firstName, lastName, expertise, enrolClassList):
        self.firstName = firstName
        self.lastName = lastName
        self.expertise = expertise
        self.enrolClassList = enrolClassList    

    def EnrolClassDisplay():
        if trainer.enrolClassList != []:
        
            print(trainer.firstName + " " + trainer.lastName + 'has enrolled the following classes.' )
        
            for i in trainer.enrolClassList:
                print(i)
        else:
            return trainer.firstName + " " + trainer.lastName + 'has not enrolled any class.'