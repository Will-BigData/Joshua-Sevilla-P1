from Database.UserDAO import UserDao
from Models.user import user
from Models.login import login
import re

class ValidationError(Exception):
    def __init__(self, message):            
        self.message = message

class UserService():
    def __init__(self, dao: UserDao):
        self.__dao = dao

    def createUser(self, name, email):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if not valid:
            raise ValidationError("Email format not correct.")
        
        new_user = user('', name, email)

        return self.__dao.createUser(new_user)
    
    def getUserByUsername(self, username):
        return self.__dao.getUserByUsername(username)
    
    def deleteUserByUsername(self, username):
        id = self.getUserByUsername(username)
        return self.__dao.deleteUser(id)

    def editUser(self, id, name, email, transactions):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if not valid:
            raise ValidationError("Email format not correct.")
        
        edit_user = user(id, name, email)
        
        return self.__dao.updateUser(edit_user)

    def loginUser(self, username, password):
        login_info = login(id, username, password)

        return self.__dao.loginUser(login_info)

    def registerUser(self, id, username, password, role):
        if password == "" or password.isspace():
           raise ValidationError("Password cannot be blank or only spaces.")

        new_login = login(id, username, password, role)

        return self.__dao.registerUser(new_login)
    
    def getLogin(self, id):
        return self.__dao.getLogin(id)
    

testdao = UserDao()
testService = UserService(testdao)

# new user 

print(testService.registerUser('testRegister1', 'password'))

id = testService.loginUser('testRegister1', 'password')


