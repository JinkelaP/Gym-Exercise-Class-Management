class groupExercise:
    def __init__(self):
        self.__className = None
        self.__trainer = None
        self.__maxCapacity = None
        self.__memberAll = None
        self.__memberWaitlist = None
        self.__feeAmount = None
        self.__memberCheckin = None

    def __str__(self):
        return (f'This is {self.__className} class. \n {self.__trainer} is the trainer. \n \
                Max {self.__maxCapacity} students allowed. \n \n')
    
    @property
    def className(self):
        return self.__className
    
    @className.setter
    def className(self, value):
        if not isinstance(value, str):
            raise ValueError('Class name must be a string!')
        self.__className = value


class member:
    def __init__(self, firstName, lastName, idNumber, enrolClassList):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__idNumber = idNumber
        self.__enrolClassList = enrolClassList

    def __str__(self):
        return (self.__idNumber, self.__firstName, self.__lastName)
    
    def enrol(groupExercise):
        pass

    def cancelEnrol(groupExercise):
        pass

    def EnrolClassDisplay(self):
        if self.enrolClassList != []:
        
            print(self.firstName + " " + self.lastName + 'has enrolled the following classes.' )
        
            for i in self.enrolClassList:
                print(i)
        else:
            return (self.firstName + " " + self.lastName + 'has not enrolled any class.')

class trainer:
    def __init__(self, firstName, lastName, expertise, enrolClassList):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__expertise = expertise
        self.__enrolClassList = enrolClassList    

    def EnrolClassDisplay(self):
        if self.enrolClassList != []:
        
            print(self.firstName + " " + self.lastName + 'has enrolled the following classes.' )
        
            for i in self.enrolClassList:
                print(i)
        else:
            return (self.firstName + " " + self.lastName + 'has not enrolled any class.')