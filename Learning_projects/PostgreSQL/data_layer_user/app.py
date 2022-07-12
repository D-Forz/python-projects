from logger import log
from user import User
from user_dao import UserDAO

option = None

while option != 5:
    print("""
    1. List Users
    2. Add User
    3. Mod User
    4. Del User
    5. Exit
    """)
    try:
        option = int(input("Choose an option: "))
    except Exception as e:
        print(f"An  error has ocurred: {e}")

    if option == 1:
        users = UserDAO.select()
        for user in users:
            log.info(user)
    elif option == 2:
        username_var = input("Write the username: ")
        password_var = input("Write the password: ")
        user = User(username=username_var, password=password_var)
        UserDAO.insert(user)
    elif option == 3:
        user_id_var = int(input("ID to modify: "))
        username_var = input("Write the new username: ")
        password_var = input("Write the new password: ")
        user = User(user_id_var, username_var, password_var)
        UserDAO.update(user)
    elif option == 4:
        user_id_var = int(input("ID to delete: "))
        user = User(user_id_var)
        UserDAO.delete(user)
    else:
        print("Please, choose a correct option")
else:
    log.info("Aplication ended.")