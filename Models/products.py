class products():
    def __init__(self, id, name, price, amount):
        self.__id__ = id
        self.__name__ = name
        self.__price = price
        self.__amount__ = amount

    def getID(self):
        return self.__id__

    def getName(self):
        return self.__name__
    
    def getPrice(self):
        return self.__price

    def getAmount(self):
        return self.__amount__
    
    def __str__(self):
        return f'ID: {self.__id__} - {self.__amount__} {self.__name__}(s) selling at ${self.__price} each'

