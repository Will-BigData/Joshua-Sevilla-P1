from Services.TransactionService import TransactionService

class transactionController():
    def __init__(self, service: TransactionService):
        self.__service = service

    def getTransactionById(self, transactionId):
        return self.__service.getTransactionById(transactionId)
    
    def getAllTransactions(self):
        return self.__service.getAllTransactions()
    
    def getUserTransactionByDate(self, userID, month, day, year):
        return self.__service.getUserTransactionByDate(userID, month, day, year)
    
    def getAllTransactionByDate(self, month, day, year):
        return self.__service.getAllTransactionByDate(month, day, year)

    def getUserTransactions(self, userID):
        return self.__service.getUserTransactions(userID)
    
    def deleteUserTransactions(self, userID):
        return self.__service.deleteUserTransactions(userID)
    
    def createTransaction(self, userID, purchased, amount, price, description):
        return self.__service.createTransaction(userID, purchased, amount, price, description)
    
    def updateTransaction(self, transactionID, purchased, amount, price, description):
        return self.__service.updateTransaction(transactionID, purchased, amount, price, description)
    
    def deleteTransaction(self, transactionID):
        return self.__service.deleteTransaction(transactionID)