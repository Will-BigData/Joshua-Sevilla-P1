from Util.connectionUtil import connectionUtility
from Models.transaction import transaction
from bson import ObjectId
import re
import logging

class TransactionsDAO():
   
    def getUserTransactions(self, userID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        logging.info("Accessing Transactions Collection...")

        results = collection.find({"userID": ObjectId(userID)})

        transactions_arr = []
        for result in results:
            new_transaction = transaction(
                result['_id'],
                result['userID'],
                result['purchased'],
                result['amount'],
                result['purchasedDate'],
                result['description'],
                result['price'])
            
            transactions_arr.append(new_transaction)
            
        client.close()
        
        return transactions_arr
    
    def createTransaction(self, new_transaction: transaction):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        result = collection.insert_one({"userID": ObjectId(new_transaction.get_userID()), "purchased": new_transaction.get_purchased(), 
                               "amount": int(new_transaction.get_amount()), "purchasedDate": new_transaction.get_purchasedDate(), "price": int(new_transaction.get_price()), "description": new_transaction.get_description()})

        client.close()

        return self.getTransaction(ObjectId(result.inserted_id))
    
    def deleteTransaction(self, transactionID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']
        
        result = collection.delete_one({"_id": ObjectId(transactionID)})

        return result.deleted_count
    
    def deleteUserTransactions(self, userID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']
        
        result = collection.delete_many({"userID": ObjectId(userID)})

        return result.deleted_count

    def updateTransaction(self, new_transaction: transaction):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        result = collection.update_one({"_id": ObjectId(new_transaction.get_transactionID())}, {"$set": {"purchased": new_transaction.get_purchased(), 
                               "amount": int(new_transaction.get_amount()), "price": int(new_transaction.get_price()), "description": new_transaction.get_description()}})

        client.close()

        return result.modified_count

    def getUserTransactionByDate(self, userID, date):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        pattern = re.compile(date, re.IGNORECASE)

        results = collection.find({"userID": ObjectId(userID), "purchasedDate": pattern})

        transactions_arr = []
        for result in results:
            new_transaction = transaction(
                result['_id'],
                result['userID'],
                result['purchased'],
                result['amount'],
                result['purchasedDate'],
                result['description'],
                result['price'])            

            transactions_arr.append(new_transaction)
            
        client.close()
        
        return transactions_arr
    
    def getAllTransactionByDate(self, date):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        pattern = re.compile(date, re.IGNORECASE)

        results = collection.find({"purchasedDate": pattern})

        transactions_arr = []
        for result in results:
            new_transaction = transaction(
                result['_id'],
                result['userID'],
                result['purchased'],
                result['amount'],
                result['purchasedDate'],
                result['description'],
                result['price'])            

            transactions_arr.append(new_transaction)
            
        client.close()
        
        return transactions_arr

    def getTransaction(self, transactionID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        result = collection.find_one({"_id": ObjectId(transactionID)})

        if result:
            found_transaction = transaction(str(result["_id"]), result["userID"], result["purchased"],
                                        result["amount"], result["purchasedDate"], result["description"], result['price'])
            client.close()
            return found_transaction
        else:
            client.close()
            return None
        
    
    def getAllTransactions(self):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['transactions']

        results = collection.find()

        transactions_arr = []
        for result in results:
            new_transaction = transaction(
                result['_id'],
                result['userID'],
                result['purchased'],
                result['amount'],
                result['purchasedDate'],
                result['description'],
                result['price'])
            
            transactions_arr.append(new_transaction)
            
        client.close()
        
        return transactions_arr


