from Database.TransactionsDAO import TransactionsDAO as Tdao

class TransactionService():
    def __init__(self, dao: Tdao):
        self.__dao = dao

    def getTransactionById(self, transactionId):
        self.__dao.getTransaction(transactionId)