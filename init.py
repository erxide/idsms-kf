import subprocess
import json
import os
import secrets
from allisok import AllIsOk
from ids import Ids
from pathlib import Path

dirparent = str(Path(__file__).parent.absolute()) + "/"

user = os.getlogin()

def generate_token(file):
    if not os.path.isfile('token/'+ file):
        tab = {'token' : secrets.token_hex(64 // 2)}
        with open('token/' + file, 'w') as f:
            json.dump(tab, f, indent=2)

def create_ids_groups():
    try:
        subprocess.run(['groupadd', '-f', 'ids'], check=True)
        print('Group ids created')
    except subprocess.CalledProcessError as e :
        exit(2)

def create_ids_user():
    try:
        subprocess.run(['useradd', '-m', '-p', '*', '-g', 'ids', 'ids'])
        print('User ids created or already exists')
    except subprocess.CalledProcessError as e: pass

def create_path_db():
    try:
        subprocess.run(['mkdir', '-p', '/var/ids'], check=True)
        print('Path /var/ids created or already exist')
    except subprocess.CalledProcessError as e :
        print('Error : ', e)
        exit(2)

def create_db_file():
    try:
        with open("/var/ids/db.json", "w") as fichier:
            json.dump({"datebuild":"","info":{}}, fichier)
        print('Database created')
    except Exception as e :
        print('Error : ', e)
        exit(2)

def create_config_file():
    if not os.path.isfile("config.json"):
        with open("config.json", "w") as fichier:
            json.dump({"files":{"test":"test.txt"},"watchport":False,"path_db": "/var/ids/","apihost":"localhost","apiport":8080}, fichier)
        print('Config file created')

def create_token_dir():
    try:
        subprocess.run(['mkdir', '-p', 'token'], check=True)
        print('Path token created or already exist')
    except subprocess.CalledProcessError:
        exit(2)

def create_raport_dir():
    try:
        subprocess.run(['mkdir', '-p', 'raport'], check=True)
        print('Path rapport created or already exist')
    except subprocess.CalledProcessError:
        exit(2)

def give_rights():
    try:
        subprocess.run(['chown', '-R', f'{user}:ids', '/var/ids'], check=True)
        subprocess.run(['chown', '-R', f'{user}:ids', '/var/ids/db.json'], check=True)
        subprocess.run(['chown', '-R', f'{user}:ids', dirparent], check=True)
        subprocess.run(['chmod', '-R', '664', '/var/ids/db.json'], check=True)
        subprocess.run(['chmod', '-R', '774', 'token/'], check=True)
        subprocess.run(['chmod', '-R', '774', 'raport/'], check=True)
        subprocess.run(['chmod', '-R', '664', 'token/tokenapi.json', 'token/tokenuser.json'], check=True)
        subprocess.run(['usermod', '-aG', 'ids', os.getlogin()], check=True)
        print('Rights given')
    except subprocess.CalledProcessError as e :
        exit(2)

def main():
    if os.geteuid() != 0:
        print("Vous devez exécuter ce programme en tant qu'administrateur (root).")
        exit(2)
    create_config_file()
    create_ids_groups()
    create_ids_user()
    create_path_db()
    create_db_file()
    create_token_dir()
    generate_token("tokenapi.json")
    generate_token("tokenuser.json")
    create_raport_dir()
    give_rights()
    if AllIsOk():
        print("All is ok")

if __name__ == "__main__":
    main()

