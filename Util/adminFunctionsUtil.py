from Util.validationError import ValidationError
from Models.user import user as usr
from Controllers.userController import userController as usC
from Controllers.transactionController import transactionController as transactionC
from Controllers.productController import productController as prC

def registerUser(user_controller: usC):
    username = input('Username: ')
    password = input('Password: ')
    
    try:
        user_controller.registerUser(username, password, 'user')
        print('Login Created!\nLogin To Create Account')
    except ValidationError as e:
        print(e.message, 'Try Again.')

def loginUser(user_controller: usC, username, password):
    user_session_id = user_controller.loginUser(username, password)

    if user_session_id == 'wrong credentials':
        print(user_session_id, '. Try again.')
        return False
    else:
        # Get users Account
        return user_controller.getAccount(user_session_id)

def createUserAccount(user_controller: usC, id):
    print('Must create an account.')
    name = input("Name: ")
    email = input("Email: ")
    try:
        account = user_controller.createUser(id, name, email)
        print('Account created! Login to start shopping!')
        return account
    except ValidationError as e:
        print(e.message)
        print('Login and try again')
        return False
    
def loginFunction(user_controller: usC):
    username = input('Username: ')
    password = input('Password: ')

    user_account = loginUser(user_controller, username, password)
    user_session_id = ''
    logged_in = False

    if type(user_account) == str:
        new_account = createUserAccount(user_controller, user_account)
        if new_account:
            user_session_id = new_account.get_id()
            logged_in = True 
    elif type(user_account) == usr:
        user_session_id = user_account.get_id()
        logged_in = True

    if logged_in:
        login_info = user_controller.getLogin(user_session_id)
        print(login_info)
        return (logged_in, user_session_id, login_info.getRole())
    else:
        return (logged_in, user_session_id, '')
    
def getAllUsers(user_controller: usC):
    arr = user_controller.getAllUsers()
    for user in arr:
        print(user)

def getAllLogins(user_controller: usC):
    arr = user_controller.getAllLogins()
    for login in arr:
        print(login)

def deleteUser(user_controller: usC, transaction_controller: transactionC, session_id):
    userID = input("input user's ID: ")
    if type(user_controller.getAccount(userID)) != str:
        try:
            user_rows = user_controller.deleteUser(session_id, userID)
            login_rows = user_controller.deleteLogin(userID)
            transaction_rows = transaction_controller.deleteUserTransactions(userID)

            print('Deleted', user_rows, 'user,', login_rows, 'login,', transaction_rows, 'transaction(s)')
        except ValidationError as e:
            print(e.message)
    else:
        print('Invalid User ID')

def findUser(user_controller: usC):
    username = input("Input user's username: ")
    print(user_controller.getUserByUsername(username))

def editUser(user_controller: usC):
    userID = input("Input user's userID: ")
    if type(user_controller.getAccount(userID)) == usr:
        old_info = user_controller.getAccount(userID)
        print("Leave blank to skip")
        name = input("Name: ")
        email = input("Email: ")
        if name == '':
            name = old_info.get_name()
        if email == '':
            email = old_info.get_email()
        try:
            print(user_controller.editUser(userID, name, email), 'rows updated')
        except ValidationError as e:
            print(e.message)
    else:
        print('Invalid user ID')

def editUserLogin(user_controller: usC):
    userID = input("Input user's userID: ")
    if type(user_controller.getAccount(userID)) == usr:
        old_info = user_controller.getLogin(userID)

        print("Leave blank to skip")
        username = input("Username ")
        password = input("Password: ")
        role = input("Role: ")

        if username == '':
            username = old_info.getUsername()
        if password == '':
            password = old_info.getPassword()
        if role == '':
            role == old_info.getRole()
        
        try:
            print(user_controller.editLogin(userID, username, password, role), 'rows updated')
        except ValidationError as e:
            print(e.message)
    else:
        print('Invalid user ID')

def getUserLogin(user_controller: usC):
    userID = input("Input user's userID: ")
    info = user_controller.getLogin(userID)
    if info:
        print(info, info.getPassword())
    else:
        print('User not found try again.')

def getAllTransactions(transaction_controller: transactionC):
    arr = transaction_controller.getAllTransactions()
    for transaction in arr:
        print(transaction)

def getAllTransactionsByDate(transaction_controller: transactionC):
    month = input("Input month: ")
    day = input("Input day: ")
    year = input("Input year (ex: 2024): ")
    try:
        arr = transaction_controller.getAllTransactionByDate(month, day, year)
        if len(arr) == 0:
            print("No transactions found")
        else:
            for transaction in arr:
                print(transaction)
    except ValidationError as e:
        print(e.message)

def getTransactionById(transaction_controller: transactionC):
    id = input('Input Transaction Id: ')   
    try:
        print(transaction_controller.getTransactionById(id))                      
    except ValidationError as e:
        print(e.message)

def getUserTransactions(transaction_controller: transactionC, user_controller: usC):
    userID = input("Input user's id: ")
    try:
        if user_controller.getAccount(userID):
            arr = transaction_controller.getUserTransactions(userID)
            for transaction in arr:
                print(transaction)
        else:
            print('Invalid user ID')
    except ValidationError as e:
        print(e.message)

def deleteAllUserTransactions(transaction_controller: transactionC, user_controller: usC):
    userID = input("Input user's id: ")
    try:
        if user_controller.getAccount(userID):
            print(transaction_controller.deleteUserTransactions(userID), 'Rows Deleted')
        else:
            print('Invalid user ID')
    except ValidationError as e:
        print(e.message)

def deleteTransaction(transaction_controller: transactionC):
    id = input('Input Transaction Id: ')
    try:
        if transaction_controller.getTransactionById(id):
            print(transaction_controller.deleteTransaction(id), ' Deleted')
        else:
            print('Invalid transaction ID')
    except ValidationError as e:
        print(e.message)

def updateTransaction(transaction_controller: transactionC):
    id = input('Input Transaction Id: ')
    try:
        transaction = transaction_controller.getTransactionById(id)
        if transaction:
            print("Leave blank to skip")
            purchased = input('Input Purchased: ')
            amount = input('Amount Purchased: ')
            price = input('Input Price: ')
            description = input("Input transaction description (Optional): ")

            if purchased == '':
                purchased = transaction.get_purchased()
            if amount == '':
                amount = transaction.get_amount()
            if description == '':
                description == transaction.get_description()
            if price == '':
                price == transaction.get_price()
            try:
                print(transaction_controller.updateTransaction(id, purchased, amount, price, description), 'rows updated')
            except ValidationError as e:
                print(e.message)
        else:
            print('Invalid transaction ID')
    except ValidationError as e:
        print(e.message)

def createTransaction(user_controller: usC, transaction_controller: transactionC):
    userID = input("Input User's ID: ")
    purchased = input("Input item purchased: ")
    amount = input("Input amount purchased: ")
    price = input('Input Price: ')
    description = input("Input transaction description (Optional): ")

    if user_controller.getLogin(userID):
        try:
            print(transaction_controller.createTransaction(userID, purchased, amount, price, description))
        except ValidationError as e:
            print(e.message)
    else:
        print("Invalid user ID")

def getAllProducts(product_controller: prC):
    arr = product_controller.getAllProducts()
    for product in arr:
        print(product)

def getProductById(product_controller: prC):
    productID = input("Product ID: ")
    try:
        print(product_controller.getProductById(productID))
    except ValidationError as e:
        print(e.message)

def createProduct(product_controller: prC):
    name = input('Input Name: ')
    price = input('Input Price: ')
    amount = input('Input Amount: ')

    try:
        product_controller.createProduct(name, price, amount)
    except ValidationError as e:
        print(e.message)

def updateProduct(product_controller: prC):
    productID = input("Input Product ID: ")
    try:
        old_product = product_controller.getProductById(productID)
        if old_product:
            print('Leave blank to skip')
            name = input('Input Name: ')
            price = input('Input Price: ')
            amount = input('Input Amount: ')

            if name == '':
                name = old_product.getName()
            if price == '':
                price = old_product.getPrice()
            if amount == '':
                amount = old_product.getAmount()

            print(product_controller.updateProduct(productID, name, price, amount, old_product.getName()), 'rows updated')
        else:
            print("Invalid Product ID")
        
    except ValidationError as e:
        print(e.message)

def deleteProduct(product_controller: prC):
    productID = input("Input Product ID: ")
    try:
        old_product = product_controller.getProductById(productID)
        if old_product:
            print(product_controller.deleteProduct(productID), 'rows deleted')
        else:
            print("Invalid Product ID")
        
    except ValidationError as e:
        print(e.message)

def getProductLikeName(product_controller: prC):
    name = input('Input search name: ')
    arr = product_controller.getProductLikeName(name)
    if len(arr) == 0:
        print("No Products Found. Search Again.")
    else:
        for product in arr:
            print(product)


