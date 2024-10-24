
class transaction():
    def __init__(self, transactionID ,userID, purchased, amount, purchasedDate, description, price):
        self.__transactionID = transactionID
        self.__userID = userID
        self.__purchased = purchased
        self.__amount = amount
        self.__purchasedDate = purchasedDate
        self.__description = description
        self.__price = price

    def get_transactionID(self):
        return self.__transactionID

    def get_userID(self):
        return self.__userID
    
    def get_purchased(self):
        return self.__purchased
    
    def get_amount(self):
        return self.__amount
    
    def get_purchasedDate(self):
        return self.__purchasedDate
    
    def get_description(self):
        return self.__description
    
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return f"TransactionID: {str(self.__transactionID)}, User: {str(self.__userID)}, | Purchased: {self.__purchased}, Amount: {self.__amount}, Purchased Date: {self.__purchasedDate}, Price: ${self.__price}, Description: {self.__description}"