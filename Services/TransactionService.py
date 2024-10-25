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
        int_values = [month, day, year]

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))
            
        if not 1900 <= int(year) <= 2100:
            raise ValidationError("Invalid Year")
            
        date_string = "{}-{}-{}".format(month, day, year)

        try:
            datetime.strptime(date_string, "%m-%d-%Y")
        except ValueError:
            raise ValidationError("Invalid Date")
        
        if not ObjectId.is_valid(userID):
            raise ValidationError("Improper user ID")
        
        return self.__dao.getUserTransactionByDate(userID, date_string)
    
    def getAllTransactionByDate(self, month, day, year):
        int_values = [month, day, year]

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))
            
        if not 1900 <= int(year) <= 2100:
            raise ValidationError("Invalid Year")
            
        date_string = "{}-{}-{}".format(month, day, year)

        try:
            datetime.strptime(date_string, "%m-%d-%Y")
        except ValueError:
            raise ValidationError("Invalid Date")
        
        return self.__dao.getAllTransactionByDate(date_string)

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
        date_now = now.strftime("%m-%d-%Y at %I:%M %p")

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
    
    def getUserTransactionsByPurchased(self, userID, name):
        return self.__dao.getTransactionsByPurchased(userID, name)
    
    def getSumOfUserTransactions(self, userID):
        if not ObjectId.is_valid(userID):
            raise ValidationError("Improper user ID")
        
        return self.__dao.getSumOfUserTransactions(userID)
    
    def getUserTotalOfEachProduct(self, userID):
        if not ObjectId.is_valid(userID):
            raise ValidationError("Improper user ID")
        
        return self.__dao.getUserTotalOfEachProduct(userID)
    
    def getSumOfAllTransactions(self):
        return self.__dao.getSumOfAllTransactions()
    
    def getTotalOfEachProduct(self):
        return self.__dao.getTotalOfEachProduct()
    
    def getTotalOfEachUser(self):
        return self.__dao.getTotalOfEachUser()
    

    