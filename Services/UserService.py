from Database.UserDAO import UserDao
from Models.user import user
from Models.login import login
from Util.validationError import ValidationError
import re

class UserService():
    def __init__(self, dao: UserDao):
        self.__dao = dao
        
    def createUser(self, id, name, email):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if not valid:
            raise ValidationError('Email format not correct')
        
        if name.isspace() or name == '':
            raise ValidationError('Must input name')
        
        new_user = user(id, name, email)

        return self.__dao.createUser(new_user)
    
    def getUserByUsername(self, username):
        return self.__dao.getUserByUsername(username)
    
    def deleteUser(self, id, userID):

        if id == userID:
            raise ValidationError('Cannot delete self')

        return self.__dao.deleteUser(userID)

    def editUser(self, id, name, email):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if not valid:
            raise ValidationError("Email format not correct.")
        
        edit_user = user(id, name, email)
        
        return self.__dao.updateUser(edit_user)

    def loginUser(self, username, password):
        login_info = login('', username, password, '')

        return self.__dao.loginUser(login_info)

    def registerUser(self, username, password, role):

        username_exists = self.__dao.getUserByUsername(username)

        if username_exists != 'No Username Found':
            raise ValidationError("Username unavailable.")
       
        if password == "" or password.isspace():
           raise ValidationError("Password cannot be blank or only spaces.")
        
        if username == "" or username.isspace():
            raise ValidationError("Username cannot be blank or only spaces.")
        
        if role not in ('admin', 'user'):
            raise ValidationError('Incorrect Role assignment')

        new_login = login('', username, password, role)

        return self.__dao.registerUser(new_login)
    
    def getAccount(self, userID):
        result = self.__dao.getUserById(userID)

        if result == 'No User Found':
            return userID
        else:
            return result
    
    def getLogin(self, id):
        return self.__dao.getLogin(id)
    
    def editLogin(self, id, username, password, role):
        new_login = login(id, username, password, role)

        if password == "" or password.isspace():
           raise ValidationError("Password cannot be blank or only spaces.")
        
        if username == "" or username.isspace():
            raise ValidationError("Username cannot be blank or only spaces.")
        
        if role not in ('admin', 'user'):
            raise ValidationError('Incorrect Role assignment')
        
        return self.__dao.editLogin(new_login)

    def deleteLogin(self, id):
        return self.__dao.deleteLogin(id)

    def getAllUsers(self):
        return self.__dao.getAllUsers()

    def getAllLogins(self):
        return self.__dao.getAllLogins()


    

if __name__ == "__main__":
    testdao = UserDao()
    testService = UserService(testdao)

    # new user 

    """ id = testService.registerUser("testUser2", "password", "user")
    if id == 'Username already exists':
        print(id)
    else:
        print(testService.createUser('johnny', 'johnnymail.com'))
        a_user = testService.getUserByUsername('testUser')
        print(a_user) """

    id = testService.loginUser('testUser2', 'password')
    print(testService.getAccount(id))
