
class login():
    def __init__(self, id, username, password, role):
        self.__id__ = id
        self.__username__ = username
        self.__password__ = password
        self.__role__ = role

    def getID(self):
        return self.__id__

    def getUsername(self):
        return self.__username__
    
    def getPassword(self):
        return self.__password__
    
    def getRole(self):
        return self.__role__
    
    def __str__(self):
        return f'{self.__username__}, Role: {self.__role__}'
    