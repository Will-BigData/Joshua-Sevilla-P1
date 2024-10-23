from Services.UserService import UserService

class userController():
    def __init__(self, userService: UserService):
        self.__userService = userService

    # login functionality
    
    def createUser(self, id, name, email):
        return self.__userService.createUser(id, name, email)
    
    def loginUser(self, username, password):
        return self.__userService.loginUser(username, password)
    
    def registerUser(self, username, password, role):
        return self.__userService.registerUser(username, password, role)
    
    def getAccount(self, userID):
        return self.__userService.getAccount(userID)
    
    # CRUD operations for Users

    def editUser(self, id, name, email):
        return self.__userService.editUser(id, name, email)
    
    def deleteUser(self, own_id, userID):
        return self.__userService.deleteUser(own_id, userID)
    
    def getUserByUsername(self, username):
        return self.__userService.getUserByUsername(username)
    
    def getLogin(self, id):
        return self.__userService.getLogin(id)
    
    def editLogin(self, id, username, password, role):
        return self.__userService.editLogin(id, username, password, role)

    def deleteLogin(self, id):
        return self.__userService.deleteLogin(id)
    
    def getAllUsers(self):
        return self.__userService.getAllUsers()
    
    def getAllLogins(self):
        return self.__userService.getAllLogins()
    




    



        