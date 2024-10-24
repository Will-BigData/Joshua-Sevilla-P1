from Database.TransactionsDAO import TransactionsDAO as Tdao
from Models.transaction import transaction
from datetime import datetime
from Util.validationError import ValidationError

class TransactionService():
    def __init__(self, dao: Tdao):
        self.__dao = dao

    def getTransactionById(self, transactionId):
        return self.__dao.getTransaction(transactionId)

    def getAllTransactions(self):
        return self.__dao.getAllTransactions()

    def getUserTransactionByDate(self, userID, month, day, year):
        try:
            date = datetime(year, month, day).strftime("%m-%d-%y")
        except ValueError:
            raise ValidationError("Invalid Date")
        
        return self.__dao.getUserTransactionByDate(userID, date)

    def getUserTransactions(self, userID):
        return self.__dao.getUserTransactions(userID)
    
    def deleteUserTransactions(self, userID):
        return self.__dao.deleteUserTransactions(userID)

    def createTransaction(self, userID, purchased, amount, description):
        now = datetime.now()
        date_now = now.strftime("%m-%d-%y")

        if amount < 0:
            raise ValidationError('Amount must be greater than 0')
        
        new_transaction = transaction('', userID, purchased, amount, date_now, description)

        return self.__dao.createTransaction(new_transaction)
    
    def updateTransaction(self, transactionID, purchased, amount, description):
        if amount < 0:
            raise ValidationError('Amount must be greater than 0')
        
        new_transaction = transaction(transactionID, '', purchased, amount, '', description)

        return self.__dao.updateTransaction(new_transaction)
    
    def deleteTransaction(self, transactionID):
        return self.__dao.deleteTransaction(transactionID)
    

    