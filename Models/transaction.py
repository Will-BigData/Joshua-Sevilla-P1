
class transaction():
    def __init__(self, userID, purchased, totalCost, purchasedDate, description):
        self.__userID = userID
        self.__purchased = purchased
        self.__totalCost = totalCost
        self.__purchasedDate = purchasedDate
        self.__description = description


    def get_userID(self):
        return self.__userID
    
    def get_purchased(self):
        return self.__purchased
    
    def get_totalCost(self):
        return self.__totalCost
    
    def get_purchasedDate(self):
        return self.__purchasedDate
    
    def get_description(self):
        return self.__description