from Database.TransactionsDAO import TransactionsDAO as Tdao
from Models.transaction import transaction
from datetime import datetime
from Util.validationError import ValidationError
from bson import ObjectId

class TransactionService():
    def __init__(self, dao: Tdao):
        self.__dao = dao

    def getTransactionById(self, transactionId):
        if not ObjectId.is_valid(transactionId):
            raise ValidationError("Improper transaction ID")
        return self.__dao.getTransaction(transactionId)

    def getAllTransactions(self):
        return self.__dao.getAllTransactions()

    def getUserTransactionByDate(self, userID, month, day, year):
        try:
            date = datetime(year, month, day).strftime("%m-%d-%y")
        except ValueError:
            raise ValidationError("Invalid Date")
        
        if not ObjectId.is_valid(userID):
            raise ValidationError("Improper user ID")
        
        return self.__dao.getUserTransactionByDate(userID, date)

    def getUserTransactions(self, userID):
        if not ObjectId.is_valid(userID):
            raise ValidationError("Improper user ID")
        return self.__dao.getUserTransactions(userID)
    
    def deleteUserTransactions(self, userID):
        if not ObjectId.is_valid(userID):
            raise ValidationError("Improper user ID")
        return self.__dao.deleteUserTransactions(userID)

    def createTransaction(self, userID, purchased, amount, price, description):
        now = datetime.now()
        date_now = now.strftime("%m-%d-%y")

        if not ObjectId.is_valid(userID):
            raise ValidationError("Improper user ID")
        
        int_values = [amount, price]

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))

        if int(amount) < 0:
            raise ValidationError('Amount must be greater than 0')
        
        if int(price) < 0:
            raise ValidationError('Price must be greater than 0')
        
        if purchased.isspace() or purchased == '':
            raise ValidationError('Item purchased is required')
        
        new_transaction = transaction('', userID, purchased, amount, date_now, description, price)

        return self.__dao.createTransaction(new_transaction)
    
    def updateTransaction(self, transactionID, purchased, amount, price, description):

        if not ObjectId.is_valid(transactionID):
            raise ValidationError("Improper transaction ID")

        int_values = [amount, price]

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))

        if int(amount) < 0:
            raise ValidationError('Amount must be greater than 0')
        
        if int(price) < 0:
            raise ValidationError('Price must be greater than 0')
        
        if purchased.isspace() or purchased == '':
            raise ValidationError('Item purchased is required')
        
        new_transaction = transaction(transactionID, '', purchased, amount, '', description, price)

        return self.__dao.updateTransaction(new_transaction)
    
    def deleteTransaction(self, transactionID):
        if not ObjectId.is_valid(transactionID):
            raise ValidationError("Improper transaction ID")
        
        return self.__dao.deleteTransaction(transactionID)
    

    