from Database.UserDAO import UserDao
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

        return self.__dao.createUser(name, email)
    
    def getUserByUsername(self, username):
        return self.__dao.getUserByUsername(username)
    
    def deleteUserByUsername(self, username):
        id = self.getUserByUsername(username)
        return self.__dao.deleteUser(id)

    def editUser(self, id, name, email, transactions):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if not valid:
            raise ValidationError("Email format not correct.")
        
        return self.__dao.updateUser(id, name, email, transactions)

    def loginUser(self, username, password):
        return self.__dao.loginUser(username, password)

    def registerUser(self, id, username, password):
        if password == "" or password.isspace():
           raise ValidationError("Password cannot be blank or only spaces.")


        return self.__dao.registerUser(id, username, password)
    

testdao = UserDao()
testService = UserService(testdao)

# new user 

print(testService.registerUser('testRegister1', 'password'))

id = testService.loginUser('testRegister1', 'password')


