from datetime import datetime
from allisok import AllIsOk
from get.getport import scan_ports
from get.create_dico import create_dico
import json


class Ids:
    def __init__(self):
        AllIsOk()
        self.config = self.open_config()
        self.files_to_check = self.config['files']
        self.lookports = self.config['watchport']
        self.path_db = self.config['path_db']
        self.file_db = self.path_db + "db.json"
        self.db = self.open_db(self.path_db + "db.json")
        self.db_data = self.db['info']



    def open_config(self):
        with open("config.json", "r") as fichier: return json.load(fichier)

    def open_db(self, path_db : str = "/var/ids/db.json"):
        with open(path_db, "r") as fichier: return json.load(fichier)

    def get_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def get_files_info(self):
        files_info = {}
        for key, value in self.files_to_check.items():
            filename = key
            filepath = value
            try:
                files_info[filename] = create_dico(filepath)
            except FileNotFoundError as e: 
                print("\033[31merror : \033[0m", e)
                exit(2)
        return files_info
    
    def create_db(self):
        data = {
            "datebuild" : self.get_time(),
            "info":{    
                "files_info" : self.get_files_info(),
                "ports" : self.getport()
            }
        }
        return data
    
    
    def getport(self):
        if self.lookports:
            return scan_ports()
        else: return []

    def build(self):
        info = self.create_db()
        with open(self.file_db, "w") as fichier:
            json.dump(info, fichier, indent=2)
        print("Database build")
        self.update_db_data()

    def update_db_data(self):
        AllIsOk()
        data = self.open_db()
        self.db_data = data['info']

    def check(self):
        if self.db_data != {}:
            pass
        else:
            print("Error : db.json is empty \nDo : python3 ids.py build before")
            exit(2)


    def checkplus(self):
        pass

    def help(self):
        pass

    def main(self):
        pass

if __name__ == "__main__":
    ids = Ids()
    ids.build()