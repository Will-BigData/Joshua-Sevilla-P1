from Util.connectionUtil import connectionUtility
from bson import ObjectId
from Models.user import user
from Models.login import login
import logging

class UserDao():

    def getUserById(self, userID) -> user:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        result = collection.find_one({"userID": ObjectId(userID)})

        if result:
            result_user = user(str(result['userID']), result['name'], result['email'])
            client.close()
            return result_user
        else:
            client.close()
            return 'No User Found'

    
    def getUserByUsername(self, username) -> user:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.find_one({"username": username})

        client.close()

        if result:
            return self.getUserById(ObjectId(result['_id']))
        else:
            return 'No Username Found'
    
    def createUser(self, new_user: user) -> user:

        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        collection.insert_one({"userID": ObjectId(new_user.get_id()), "name": new_user.get_name(), "email": new_user.get_email()})

        client.close()

        return self.getUserById(new_user.get_id())

    def deleteUser(self, userID) -> int:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        result = collection.delete_one({"userID": ObjectId(userID)})

        client.close()

        return result.deleted_count

    def updateUser(self, edit_user: user) -> int:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        result = collection.update_one({"userID": ObjectId(edit_user.get_id())}, {"$set": {"name": edit_user.get_name(), "email": edit_user.get_email()}})

        client.close()

        return result.modified_count
    
    def loginUser(self, login_info: login) -> str:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.find_one({"username": login_info.getUsername(), "password": login_info.getPassword()})

        client.close()

        if result:
            return str(result['_id'])
        else:
            return 'wrong credentials'
    
    def registerUser(self, new_login: login) -> str:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.insert_one({"username": new_login.getUsername(), "password": new_login.getPassword(), "role": new_login.getRole()})

        client.close()

        return result.inserted_id
        
    def deleteLogin(self, id) -> int:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.delete_one({"_id": ObjectId(id)})

        client.close()

        return result.deleted_count
    
    def editLogin(self, new_login: login) -> int:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.update_one({"_id": ObjectId(new_login.getID())}, 
                                       {"$set": {"username": new_login.getUsername(), "password": new_login.getPassword(), "role": new_login.getRole()}})
        
        return result.modified_count
    
    def getLogin(self, id) -> login:
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.find_one({"_id": ObjectId(id)})

        login_details = login(str(result['_id']), result['username'], result['password'], result['role'])

        return login_details
    
    def getAllUsers(self):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        results = collection.find()

        user_arr = []
        for result in results:
            result_user = user(str(result['userID']), result['name'], result['email'])

            user_arr.append(result_user)

        client.close()

        return user_arr
    
    def getAllLogins(self):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        results = collection.find()

        login_arr = []
        for result in results:
            result_login = login(str(result['_id']), result['username'], result['password'], result['role'])

            login_arr.append(result_login)

        client.close()

        return login_arr


