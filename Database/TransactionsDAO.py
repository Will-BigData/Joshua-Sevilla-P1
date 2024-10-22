from Util.connectionUtil import connectionUtility
from Models.transaction import transaction
from datetime import datetime
from bson import ObjectId

class TransactionsDAO():
   
    def getUserTransactions(self, userID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        results = collection.find({"userID": userID})

        transactions_arr = []
        for result in results:
            new_transaction = transaction(
                result['_id'],
                result['userID'],
                result['purchased'],
                result['amount'],
                result['purchasedDate'],
                result['description'])
            

            transactions_arr.append(new_transaction)
            
        client.close()
        
        return transactions_arr
    
    def createTransaction(self, userID, purchased, amount, description):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        now = datetime.now()

        date_now = now.strftime("%m-%d-%y")

        result = collection.insert_one({"userID": userID, "purchased": purchased, 
                               "amount": amount, "purchasedDate": date_now, "description": description})

        client.close()

        return self.getTransaction(result.inserted_id)
    
    def deleteTransaction(self, userID):
        pass

    def updateTransaction(self, userID):
        pass

    def getUserTransactionByDate(self, userID, month, date, year):
        pass

    def getTransaction(self, transactionID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        result = collection.find_one({"_id": ObjectId(transactionID)})

        found_transaction = transaction(str(result["_id"]), result["userID"], result["purchased"],
                                        result["amount"], result["purchasedDate"], result["description"])
        
        client.close()

        return found_transaction


userID = '6716f69eefde3f524d8be6ab'
object_id = ObjectId(userID)
testDao = TransactionsDAO()

# new_transaction = testDao.createTransaction(object_id, 'Apple', 30, 'test')

# print(new_transaction)
transactions = testDao.getUserTransactions(object_id)
for x in transactions:
    print(x)
