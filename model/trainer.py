import model.groupExercise as gE

class Trainer:
    def __init__(self, firstName, lastName, expertise):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__expertise = expertise
        self.__enrolClassList = []

    def __str__(self):
        return self.__firstName + ' ' + self.__lastName + ' ' + self.__expertise
    
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
    def expertise(self):
        return self.__expertise
    
    @expertise.setter
    def expertise(self, value):
        if not isinstance(value, str):
            raise ValueError('Expertise must be a string!')
        self.__expertise = value
    
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
    def enrolClassDisplay(self):
        if self.__enrolClassList != []:
        
            print(self.__firstName + " " + self.__lastName + ' has been assigned to the following classes.' )
        
            for i in self.enrolClassList:
                print(i.className)
            return 'Press enter to return.'
        else:
            return (self.__firstName + " " + self.__lastName + ' has not been assigned to any class.')
        
    def enrol(self, groupExercise):
        if groupExercise not in self.__enrolClassList:
            self.__enrolClassList.append(groupExercise)
        else:
            pass
