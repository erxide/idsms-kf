import os

def config_is_here():
    if not os.path.isfile("config.json"): 
        print("Error : config.json doesn't exist \nDo : sudo python3 init.py") 
        raise FileNotFoundError

def db_is_here():
    if not os.path.isfile("/var/ids/db.json"): 
        print("Error : db.json doesn't exist \nDo : sudo python3 init.py")
        raise FileNotFoundError

def tokenapi_is_here():
    if not os.path.isfile("token/tokenapi.json"): 
        print("Error : api token doesn't exist \nDo : sudo python3 init.py")
        raise FileNotFoundError

def tokenuser_is_here():
    if not os.path.isfile("token/tokenuser.json"): 
        print("Error : user api token doesn't exist \nDo : sudo python3 init.py")
        raise FileNotFoundError
    
def getdir_is_here():
    if not os.path.isdir("get/"): 
        print("Error : get directory doesn't exist")
        raise FileNotFoundError

def AllIsOk(forapi : str = ''):
    try:
        config_is_here()
        db_is_here()
        config_is_here()
        db_is_here()
        getdir_is_here()
        if forapi != '':
            tokenapi_is_here()
            tokenuser_is_here()
        return True
    except FileNotFoundError:
        exit(2)

if __name__ == "__main__":
    if AllIsOk():
        print("All is ok")