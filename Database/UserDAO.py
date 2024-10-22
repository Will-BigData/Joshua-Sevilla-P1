from Util.connectionUtil import connectionUtility
from bson import ObjectId
from Models.user import user
import logging

class UserDao():

    def getUserById(self, userID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        result = collection.find_one({"userID": ObjectId(userID)})
        result_user = user(result['name'], result['email'])

        client.close()

        return result_user
    
    def getUserByUsername(self, username):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.find_one({"username": username})

        client.close()

        if result:
            return self.getUserById(result['_id']) 
        else:
            return 'No Username Found'
    
    def createUser(self, userID, name, email):

        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        result = collection.insert_one({"userID": userID, "name": name, "email": email})

        client.close()

        return self.getUserById(result.inserted_id)

    def deleteUser(self, userID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        result = collection.delete_one({"userID": userID})

        client.close()

        return result.deleted_count

    def updateUser(self, userId, name, email):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['Users']

        result = collection.update_one({"userID": userId}, {"$set": {"name": name, "email": email}})

        client.close()

        return result.modified_count
    
    def loginUser(self, username, password):

        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.find_one({"username": username, "password": password})

        client.close()

        if result:
            print('logged in')
            return result['_id']
        else:
            return 'wrong credentials'
    
    def registerUser(self, username, password, role):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.find_one({"username": username})

        if result:
            client.close()
            return 'Username already exists'
        else:
            result = collection.insert_one({"username": username, "password": password, "role": role})
            client.close()

            return result.inserted_id
        
    def deleteLogin(self, id):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['login']

        result = collection.delete_one({"_id": id})

        client.close()

        return result.deleted_count
        
        

testDao = UserDao()
""" id = testDao.registerUser("testUser", "password", "user")
print(id)
testDao.createUser(id, 'john', 'john@gmail.com') """

a_user = testDao.getUserByUsername('admin')
print(a_user.get_name() + " " + a_user.get_email())
