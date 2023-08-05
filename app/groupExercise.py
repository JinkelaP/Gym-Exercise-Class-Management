class groupExercise:
    def __init__(self):
        self.__className = None
        self.__trainer = None
        self.__maxCapacity = None
        self.__memberAll = []
        self.__memberWaitlist = []
        self.__feeAmount = None
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
        if not isinstance(value, object):
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
    def feeAmount(self):
        return self.__feeAmount
    
    @feeAmount.setter
    def feeAmount(self, value):
        if not isinstance(value, int):
            raise ValueError('Fee Amount must be a number!')
        self.__feeAmount = value

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

    
