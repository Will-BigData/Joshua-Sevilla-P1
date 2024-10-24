from Database.UserDAO import UserDao
from Database.TransactionsDAO import TransactionsDAO
from Services.UserService import UserService
from Services.TransactionService import TransactionService
from Controllers.userController import userController as usC
from Controllers.transactionController import transactionController as transactionC
from Models.user import user as usr
from Services.UserService import ValidationError
from Util.adminFunctionsUtil import *

def main():

    print("Welcome To Client Side Store:")

    user_dao = UserDao()
    transaction_dao = TransactionsDAO()
    transaction_service = TransactionService(transaction_dao)
    user_service = UserService(user_dao)
    user_controller = usC(user_service)
    transaction_controller = transactionC(transaction_service)

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
                logged_in_selection = input('Selections: u = user functions, t = transaction functions, q = logout:\n')
                
                if logged_in_selection == 'u':
                    function_selection = input('u = Get all users, l = Get all logins, d = delete user, f = find user, e = edit user, x = edit login, p = get login, any other key = back:\n')
                    match function_selection:
                        case 'u': 
                            getAllUsers(user_controller)
                        case 'l':
                            getAllLogins(user_controller)
                        case 'd':
                            deleteUser(user_controller, transaction_controller, session_id)
                        case 'f':
                            username = input("Input user's username: ")
                            print(user_controller.getUserByUsername(username))
                        case 'e':
                            editUser(user_controller)
                        case 'x':
                            editLogin(user_controller)
                        case 'p':
                            getLogin(user_controller)
                        case _:
                            pass
                
                elif logged_in_selection == 't':
                    function_selection = input('t = Get all transactions, i = Get transaction by id, g = Get user transactions, x = delete all user transactions, d = Delete transaction, u = Update transaction, any other key = back:\n')
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
                        case _:
                            pass
                elif logged_in_selection == 'q':
                    break
                else:
                    print("Not an option try again")
                

        elif login_selection == 'r':
            username = input('Username: ')
            password = input('Password: ')
            
            try:
                user_controller.registerUser(username, password, 'user')
                print('Login Created!\nLogin To Create Account')
            except ValidationError as e:
                print(e.message, 'Try Again.')

        elif login_selection == 'q':
            print('See you next time')
        else:
            print('Incorrect input try again. ')



if __name__ == '__main__':
    main()