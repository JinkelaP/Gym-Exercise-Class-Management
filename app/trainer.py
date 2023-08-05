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