from serviceapi.get_all_users import get_all_users
import os

def ask_username():
    while True:
        try :
            username = input("Please choose a user for the service, press Enter without typing anything to select your username : ")
            all_users = get_all_users()
            if username == "":
                return os.getlogin()
            elif not username in all_users:
                print("Please choose a valid user : ", all_users)
            elif username in all_users:
                return username
        except KeyboardInterrupt:
            print("\n")
            exit(1)