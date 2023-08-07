class GroupExercise:
    def __init__(self, className, maxCapacity):
        self.__className = className
        self.__trainer = None
        self.__maxCapacity = maxCapacity
        self.__memberAll = []
        self.__memberWaitlist = []
        self.__fee = None
        self.__memberCheckin = []

    def __str__(self):
        return (f'This is {self.__className} class.\n{self.__trainer} is the trainer.\n\
Max {self.__maxCapacity} students allowed.')
    
    #----------------------------------------------
    # getter and setter for each attributes

    @property
    def className(self):
        return self.__className
    
    @className.setter
    def className(self, value):
        if not isinstance(value, str):
            raise ValueError('Class name must be a string!')
        self.__className = value

    @property
    def trainer(self):
        return self.__trainer
    
    @trainer.setter
    def trainer(self, value):
        if not isinstance(value, Trainer):
            raise ValueError('Trainer must be a trainer object!')
        self.__trainer = value

    @property
    def maxCapacity(self):
        return self.__maxCapacity
    
    @maxCapacity.setter
    def maxCapacity(self, value):
        if not isinstance(value, int):
            raise ValueError('Max Capacity of the class must be a number!')
        self.__maxCapacity = value

    @property
    def memberAll(self):
        return self.__memberAll
    
    @memberAll.setter
    def memberAll(self, value):
        if not isinstance(value, list):
            raise ValueError('Class member list must be a list!')
        self.__memberAll = value

    @property
    def memberWaitlist(self):
        return self.__memberWaitlist
    
    @memberWaitlist.setter
    def memberWaitlist(self, value):
        if not isinstance(value, list):
            raise ValueError('The waitlist must be a list!')
        self.__memberWaitlist = value

    @property
    def fee(self):
        return self.__fee
    
    @fee.setter
    def fee(self, value):
        if not isinstance(value, int):
            raise ValueError('Fee must be a number!')
        self.__fee = value

    @property
    def memberCheckin(self):
        return self.__memberCheckin
    
    @memberCheckin.setter
    def memberCheckin(self, value):
        if not isinstance(value, list):
            raise ValueError('Checked-in member list must be a list!')
        self.__memberCheckin = value

    #----------------------------------------------
    # methods below

    
    def enrol(self, member):
        currentCapacity = len(self.memberAll)
        if currentCapacity < self.maxCapacity:
            self.__memberAll.append(member)
            return (member.firstName + ' has been added to the enrolled list of ' + self.__className + '!')
        else:
            while True:
                userInput = input('Unfortunately the class has been fully enrolled.\nAre you happy to be added to the waitlist? (y/n)')
                if userInput.upper() == 'Y' or userInput.upper() == 'YES':
                    self.__memberWaitlist.append(member)
                    return (member.firstName + ' has been added to the waitlist of ' + self.__className + '!')
                elif userInput.upper() == 'N' or userInput.upper() == 'NO':
                    return 'Class enrolment cancelled.'
                else:
                    print('Please re-enter.')

    def removeMember(self, member):
        if member in self.__memberAll:
            self.__memberAll.remove(member)
            return (member + ' has been removed from the enrolled list.')
        else:
            return (member + ' is not in the enrolled list')
        
    def displayEnrolled(self):
        print('All gym members currently enrolled in ' + self.__className)
        for member in self.__memberAll:
            print(member)
    
    def assignTrainer(self, t):
        if not isinstance(t, Trainer):
            raise ValueError('Trainer must be a trainer object!')
        self.__trainer = t
        return (t + ' has been assigned as the trainer of ' + self.__className)
    
    def numberEnrolled(self):
        return (str(len(self.__memberAll)) + ' members has enrolled in the class!')
    
    def numberAvailable(self):
        available = self.__maxCapacity - len(self.__memberAll)
        return (str(available) + ' slots available for enrolment!')
    
    def setFee(self, fee):
        if not isinstance(fee, (int, float)):
            raise ValueError('Fee must be a number!')
        self.__fee = fee
        return ('Fee set.')

    def totalPayment(self):
        total = len(self.__memberAll) * self.__fee
        return ('The total payment received is ' + total + ' NZD.')
    
    def markAttendance(self, member):
        if member in self.__memberAll:
            self.__memberCheckin.append(member)
            return (member.firstName + "'s attendance has been marked.")
        else:
            return (f"Caution: you cannot mark {member.firstName}'s attendance because {member.firstName} is not in the enrolled list.")
        
    def attendanceClass(self):
            return ('The attendance of the class is '+ str(round(len((self.__memberAll) / len(self.__memberAll))* 100), 2) + '%')