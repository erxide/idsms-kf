import subprocess
import json

def create_ids_groups():
    try:
        subprocess.run(['groupadd', 'ids'], check=True)
    except subprocess.CalledProcessError as e :
        exit(2)

def create_ids_user():
    try:
        subprocess.run(['useradd', '-m', '-p', '*', '-G', 'ids', 'ids'], check=True)
    except subprocess.CalledProcessError as e :
        exit(2)

def create_path_db():
    try:
        subprocess.run(['mkdir', '/var/ids'], check=True)
    except subprocess.CalledProcessError as e :
        exit(2)

def create_db():
    try:
        with open("/var/ids/db.json", "w") as fichier:
            json.dump({}, fichier)
    except Exception as e :
        print('Error : ', e)
        exit(2)

def give_rights():
    try:
        subprocess.run(['chown', '-R', 'ids:ids', '/var/ids'], check=True)
    except subprocess.CalledProcessError as e :
        exit(2)

def main():
    create_ids_groups()
    create_ids_user()
    create_path_db()
    create_db()
    give_rights()

if __name__ == "__main__":
    main()

