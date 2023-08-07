class member:
    def __init__(self):
        self.__firstName = None
        self.__lastName = None
        self.__idNumber = None
        self.__enrolClassList = []

    def __str__(self):
        return (self.__idNumber, self.__firstName, self.__lastName)
    
    #----------------------------------------------
    # getter and setter for each attributes
    
    @property
    def firstName(self):
        return self.__firstName
    
    @firstName.setter
    def firstName(self, value):
        if not isinstance(value, str):
            raise ValueError('First name must be a string!')
        self.__firstName = value

    @property
    def lastName(self):
        return self.__lastName
    
    @lastName.setter
    def lastName(self, value):
        if not isinstance(value, str):
            raise ValueError('Last name must be a string!')
        self.__lastName = value
    
    @property
    def idNumber(self):
        return self.__idNumber
    
    @idNumber.setter
    def idNumber(self, value):
        if not isinstance(value, int):
            raise ValueError('ID number must be a number!')
        self.__idNumber = value
    
    @property
    def enrolClassList(self):
        return self.__enrolClassList
    
    @enrolClassList.setter
    def enrolClassList(self, value):
        if not isinstance(value, list):
            raise ValueError('enrolClassList must be a list!')
        self.__enrolClassList = value
    

    #----------------------------------------------
    # methods below
    




    def cancelEnrol(groupExercise):
        pass

    def EnrolClassDisplay(self):
        if self.enrolClassList != []:
        
            print(self.firstName + " " + self.lastName + 'has enrolled the following classes.' )
        
            for i in self.enrolClassList:
                print(i)
        else:
            return (self.firstName + " " + self.lastName + 'has not enrolled any class.')

