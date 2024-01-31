import subprocess
import json

def create_ids_groups():
    try:
        subprocess.run(['groupadd', '-f', 'ids'], check=True)
        print('Group ids created')
    except subprocess.CalledProcessError as e :
        exit(2)

def create_ids_user():
    try:
        subprocess.run(['useradd', '-m', '-p', '*', '-g', 'ids', 'ids'], check=True)
        print('User ids created or already exists')
    except subprocess.CalledProcessError as e:
        if "useradd: existing lock file" not in str(e.stderr):
            print(f"Erreur lors de la création de l'utilisateur : {e}")

def create_path_db():
    try:
        subprocess.run(['mkdir', '-p', '/var/ids'], check=True)
        print('Path /var/ids created or already exist')
    except subprocess.CalledProcessError as e :
        print('Error : ', e)
        exit(2)

def create_db():
    try:
        with open("/var/ids/db.json", "w") as fichier:
            json.dump({}, fichier)
        print('Database created')
    except Exception as e :
        print('Error : ', e)
        exit(2)

def give_rights():
    try:
        subprocess.run(['chown', '-R', 'ids:ids', '/var/ids'], check=True)
        print('Rights given')
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

