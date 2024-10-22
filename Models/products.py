class products():
    def __init__(self, name, amount):
        self.__name__ = name
        self.__amount__ = amount

    def getName(self):
        return self.__name__

    def setAmount(self):
        return self.__amount__

    def setName(self, name):
        self.__name__ = name

    def setAmount(self, amount):
        self.__amount__ = amount
