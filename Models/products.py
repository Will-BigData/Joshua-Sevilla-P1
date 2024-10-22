class products():
    def __init__(self, name, amount):
        self.__name__ = name
        self.__amount__ = amount

    def getName(self):
        return self.__name__

    def getAmount(self):
        return self.__amount__
    
    def __str__(self):
        return f'{self.__amount__} {self.__name__}(s)'

