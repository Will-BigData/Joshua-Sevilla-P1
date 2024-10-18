
class user():
    def __init__(self, name, email, transactions):
        self.__name = name
        self.__email = email
        self.__transactions = transactions

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_transactions(self):
        return self.__transactions
    
    
        
