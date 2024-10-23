from Database.UserDAO import UserDao
from Database.TransactionsDAO import TransactionsDAO
from Services.UserService import UserService
from Services.TransactionService import TransactionService
from Controllers.userController import userController as usC
from Models.user import user
from Services.UserService import ValidationError

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
        print('Account created!')
        return account
    except ValidationError as e:
        print(e.message)
        print('Log in and try again')
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
    elif type(user_account) == user:
        user_session_id = user_account.get_id()
        logged_in = True

    if logged_in:
        login_info = user_controller.getLogin(user_session_id)
        print(login_info)
        return (logged_in, user_session_id, login_info.getRole())
    else:
        return (logged_in, user_session_id, '')

def main():

    print("Welcome To Client Side Store:")

    user_dao = UserDao()
    transaction_dao = TransactionsDAO()
    transaction_service = TransactionService(transaction_dao)
    user_service = UserService(user_dao)
    user_controller = usC(user_service)

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
                    function_selection = input('u = Get all users, l = Get all logins, d = delete user f = find user, e = edit user, x = edit login, p = get login, any other key = back:\n')
                    match function_selection:
                        case 'u': 
                            arr = user_controller.getAllUsers()
                            for user in arr:
                                print(user)
                        case 'l':
                            arr = user_controller.getAllLogins()
                            for login in arr:
                                print(login)
                        case 'd':
                            userID = input("input user's ID: ")
                            try:
                                user_controller.deleteUser(session_id, userID)
                                user_controller.deleteLogin(userID)
                                print("Delete Successfull")
                            except ValidationError as e:
                                print(e.message)

                            # DELETE TRANSACTIONS
                            
                           
                        case 'f':
                            username = input("Input user's username: ")
                            print(user_controller.getUserByUsername(username))
                        case 'e':
                            userID = input("Input user's userID: ")
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
                        case 'x':
                            userID = input("Input user's userID: ")
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

                        case 'p':
                            userID = input("Input user's userID: ")
                            info = user_controller.getLogin(userID)
                            if info:
                                print(info, info.getPassword())
                            else:
                                print('User not found try again.')

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