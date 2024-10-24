from Database.UserDAO import UserDao
from Database.TransactionsDAO import TransactionsDAO
from Database.ProductsDAO import ProductsDAO
from Services.UserService import UserService
from Services.TransactionService import TransactionService
from Services.ProductService import ProductsService
from Controllers.userController import userController as usC
from Controllers.transactionController import transactionController as transactionC
from Controllers.productController import productController as pC
from Util.adminFunctionsUtil import *
from Util.userFunctions import *

def main():

    print("Welcome To Client Side Store:")

    user_dao = UserDao()
    user_service = UserService(user_dao)
    user_controller = usC(user_service)

    transaction_dao = TransactionsDAO()
    transaction_service = TransactionService(transaction_dao)
    transaction_controller = transactionC(transaction_service)

    product_dao = ProductsDAO()
    product_service = ProductsService(product_dao)
    product_controller = pC(product_service)

    login_selection = ''

    while(login_selection != 'q'):
        login_selection = input('Select: [a] = login, [r] = register, [q] = quit\n')

        if login_selection == 'a':
            logged_in = loginFunction(user_controller)
            logged_in_selection = ''

            is_logged_in = logged_in[0]
            session_id = logged_in[1]
            role = logged_in[2]

            # admin features
            while(is_logged_in and logged_in_selection != 'q' and role == 'admin'):
                logged_in_selection = input('Selections: u = User Functions, t = Transaction Functions, p = Product Functions, q = Logout:\n')
                if logged_in_selection == 'u':
                    function_selection = input('u = Get All Users, l = Get All Logins, d = Delete User, f = Find User, e = Edit User, x = Edit Login, p = Get Login, Other = back:\n')
                    match function_selection:
                        case 'u': 
                            getAllUsers(user_controller)
                        case 'l':
                            getAllLogins(user_controller)
                        case 'd':
                            deleteUser(user_controller, transaction_controller, session_id)
                        case 'f':
                            findUser(user_controller)
                        case 'e':
                            editUser(user_controller)
                        case 'x':
                            editUserLogin(user_controller)
                        case 'p':
                            getUserLogin(user_controller)
                        case _:
                            pass
                elif logged_in_selection == 't':
                    function_selection = input('t = Get All Transactions, i = Get Transaction by ID, g = Get User Transactions, x = Delete All User transactions,\nd = Delete transaction, u = Update Transaction, c = Create Transaction, m = Get All Transactions By Date, Other = back:\n')
                    match function_selection:
                        case 't':
                            getAllTransactions(transaction_controller)
                        case 'i':
                            getTransactionById(transaction_controller)
                        case 'g':
                            getUserTransactions(transaction_controller, user_controller)
                        case 'x':
                            deleteAllUserTransactions(transaction_controller, user_controller)
                        case 'd':
                            deleteTransaction(transaction_controller)
                        case 'u':
                            updateTransaction(transaction_controller)
                        case 'c':
                            createTransaction(user_controller, transaction_controller)
                        case 'm':
                            getAllTransactionsByDate(transaction_controller)
                        case _:
                            pass
                elif logged_in_selection == 'p':
                    function_selection = input('p = Get All Products, i = Get Product by ID, c = Create Product, u = Update Product, n = Get Products By Name, d = Delete Product, Other = back:\n')
                    match function_selection:
                        case 'p':
                            getAllProducts(product_controller)
                        case 'i':
                            getProductById(product_controller)
                        case 'c':
                            createProduct(product_controller)
                        case 'u':
                            updateProduct(product_controller)
                        case 'n':
                            getProductLikeName(product_controller)
                        case 'd':
                           deleteProduct(product_controller)
                        case _:
                            pass
                elif logged_in_selection == 'q':
                    break
                else:
                    print("Not an option try again")
            
            # user
            while(is_logged_in and logged_in_selection != 'q' and role == 'user'):
                logged_in_selection = input('Selections: u = User Functions, t = Transaction Functions, p = Product Functions, q = Logout:\n')
                if logged_in_selection == 'u':
                    function_selection = input('v = View Account, l = View Login, a = Update account, k = Update Login:\n')
                    match function_selection:
                        case 'v':
                            getAccount(user_controller, session_id)
                        case 'l':
                            getLogin(user_controller, session_id)
                        case 'a':
                            editAccount(user_controller, session_id)
                        case 'k':
                            editLogin(user_controller, session_id)
                        case _:
                            pass                       
                elif logged_in_selection == 't':
                    function_selection = input('v = View Transactions, u = Update Transaction, i = Get Transaction By ID, g = Get Transactions By Date, d = Delete Transactions, Other = back:\n')
                    match function_selection:
                        case 'v':
                            viewTransactions(transaction_controller, user_controller, session_id)
                        case 'u':
                            updateTransaction(transaction_controller)
                        case 'i':
                            getTransactionById(transaction_controller)
                        case 'd':
                            deleteTransaction(transaction_controller)
                        case 'g':
                            getAllUserTransactionsByDate(user_controller, transaction_controller, session_id)
                        case _:
                            pass   
                elif logged_in_selection == 'p':
                    function_selection = input('v = View Products, p = Purchase Products, s = Search Product Name, Other = back: \n')
                    match function_selection:
                        case 'v':
                            getAllProducts(product_controller)
                        case 's':
                            getProductLikeName(product_controller)
                        case 'p':
                            purchaseProduct(product_controller, transaction_controller, session_id)
                        case _:
                            pass
                elif logged_in_selection == 'q':
                    break
                else:
                    print("Not an option try again")

        elif login_selection == 'r':
            registerUser(user_controller)
        elif login_selection == 'q':
            print('See you next time')
        else:
            print('Incorrect input try again. ')



if __name__ == '__main__':
    main()