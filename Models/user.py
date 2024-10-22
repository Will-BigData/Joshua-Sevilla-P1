
class user():
    def __init__(self, id, name, email):
        self.__id = id
        self.__name = name
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def __str__(self):
        return f'Name: {self.__name}, Email: {self.__email}'
    
    
   
    
        
