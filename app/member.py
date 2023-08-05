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

