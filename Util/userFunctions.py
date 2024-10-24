from Util.validationError import ValidationError
from Models.user import user as usr
from Controllers.userController import userController as usC
from Controllers.transactionController import transactionController as transactionC
from Controllers.productController import productController as prC

def getAccount(user_controller: usC, session_id):
    print(user_controller.getAccount(session_id))

def getLogin(user_controller: usC, session_id):
    login = user_controller.getLogin(session_id)
    print(login, ',Password:', login.getPassword())

def editAccount(user_controller: usC, session_id):
    if type(user_controller.getAccount(session_id)) == usr:
        old_info = user_controller.getAccount(session_id)
        print("Leave blank to skip")
        name = input("Name: ")
        email = input("Email: ")
        if name == '':
            name = old_info.get_name()
        if email == '':
            email = old_info.get_email()
        try:
            print(user_controller.editUser(session_id, name, email), 'rows updated')
        except ValidationError as e:
            print(e.message)
    else:
        print('Invalid user ID')

def editLogin(user_controller: usC, session_id):
    if type(user_controller.getAccount(session_id)) == usr:
        old_info = user_controller.getLogin(session_id)

        print("Leave blank to skip")
        username = input("Username ")
        password = input("Password: ")

        if username == '':
            username = old_info.getUsername()
        if password == '':
            password = old_info.getPassword()
        
        try:
            print(user_controller.editLogin(session_id, username, password, old_info.getRole()), 'rows updated')
        except ValidationError as e:
            print(e.message)
    else:
        print('Invalid user ID')

def getAllUserTransactionsByDate(user_controller: usC, transaction_controller: transactionC, session_id):
    try:
        if user_controller.getAccount(session_id):
            month = input("Input month: ")
            day = input("Input day: ")
            year = input("Input year (ex: 2024): ")
            arr = transaction_controller.getUserTransactionByDate(session_id, month, day, year)
            if len(arr) == 0:
                print("No transactions found")
            else:
                for transaction in arr:
                    print(transaction)
        else:
            print('Invalid user ID')
    except ValidationError as e:
        print(e.message)

def viewTransactions(transaction_controller: transactionC, user_controller: usC, session_id):
    try:
        if user_controller.getAccount(session_id):
            arr = transaction_controller.getUserTransactions(session_id)
            for transaction in arr:
                print(transaction)
        else:
            print('Invalid user ID')
    except ValidationError as e:
        print(e.message)

def purchaseProduct(product_controller: prC, transaction_controller: transactionC, session_id):
    search = input("Input product name or ID to buy: ")
    name_search_result = product_controller.doesProductNameExist(search)

    try:
        id_search_result = product_controller.getProductById(search)
    except ValidationError as e:
        id_search_result = None

    if name_search_result:
        if name_search_result.getAmount() < 0:
            print("Cannot purchase because product is out of stock.")
            return
        
        amount_to_buy = input("Input amount to buy: ")

        if int(name_search_result.getAmount()) - int(amount_to_buy) < 0:
            print("Cannot purchase more items than in stock of product.")
            return
        
        description = input("Input transaction description (Optional): ")
        price = int(amount_to_buy) * name_search_result.getPrice()
        new_amount = name_search_result.getAmount() - int(amount_to_buy)

        print('Purchasing:', name_search_result.getName(), '\nPrice:', name_search_result.getPrice(), '\nAmount:', amount_to_buy,
                '\nPrice:', price,'\nDescription:', description)
        
        confirmation = input("Confirm order by typing y and other to cancel: ")
        if confirmation == 'y':
            try:
                transaction_controller.createTransaction(session_id, name_search_result.getName(), amount_to_buy, price, description)
                product_controller.updateProduct(name_search_result.getID(), name_search_result.getName(),
                                                name_search_result.getPrice(), new_amount, name_search_result.getName())
            except ValidationError as e:
                print(e.message)
        else:
            print('Order cancelled')
    elif id_search_result:
        if id_search_result.getAmount() < 0:
            print("Cannot purchase because product is out of stock.")
            return
        
        amount_to_buy = input("Input amount to buy: ")

        if int(id_search_result.getAmount()) - int(amount_to_buy) < 0:
            print("Cannot purchase more items than in stock of product.")
            return
        
        description = input("Input transaction description (Optional): ")
        price = int(amount_to_buy) * id_search_result.getPrice()
        new_amount = id_search_result.getAmount() - int(amount_to_buy)

        print('Purchasing:', id_search_result.getName(), '\nPrice:', id_search_result.getPrice(), '\nAmount:', amount_to_buy,
                '\nPrice:', price,'\nDescription:', description)
        
        confirmation = input("Confirm order by typing y and other to cancel: ")
        if confirmation == 'y':
            try:
                transaction_controller.createTransaction(session_id, id_search_result.getName(), amount_to_buy, price, description)
                product_controller.updateProduct(id_search_result.getID(), id_search_result.getName(),
                                                id_search_result.getPrice(), new_amount, id_search_result.getName())
            except ValidationError as e:
                print(e.message)
        else:
            print('Order cancelled')
    else:
        print("Product doesn't exist")