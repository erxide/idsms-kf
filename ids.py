from datetime import datetime
from deepdiff import DeepDiff
import os
import secrets
from sys import argv
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
        AllIsOk()
        info = self.create_db()
        with open(self.file_db, "w") as fichier:
            json.dump(info, fichier, indent=2)
        self.update_db_data()
        return "Database build"

    def update_db_data(self):
        AllIsOk()
        data = self.open_db()
        self.db_data = data['info']

    def check(self):
        AllIsOk()
        if self.db_data != {}:
            info = self.create_db()
            if self.db_data == info['info']:
                return {"state" : "ok"}
            else:
                self.raport(info)
                return {"state" : "divergent"}
        else:
            print("Error : db.json is empty \nDo : python3 ids.py build before")
            exit(2)

    def raport(self, info):
        AllIsOk()
        diffs = {
            "check date":self.get_time(),
            "diff":self.checkplus(info)}
        namerappor = secrets.token_hex(8 // 2)
        with open("raport/" + namerappor + ".json", "w") as fichier:
            json.dump(diffs, fichier, indent=2)

    def checkplus(self, info):
        diffs = []
        diff = DeepDiff(self.db_data, info['info'])
        for firstkey, value in diff.get('values_changed', {}).items():
            diffs.append(f"The value of {firstkey} has changed from {value['old_value']} to {value['new_value']}.")
        return diffs

    def help(self):
        print("Usage: python ids.py [command]")
        print("Commandes:")
        print("  build, b: Construit le fichier réference")
        print("  check, c: Vérifie les fichiers sont toujours intègres")

    def main(self):
        if len(argv) > 1:
            cmd = argv[1]
            if cmd == 'build' or cmd == 'b': print(self.build())
            elif cmd == 'check'or cmd == 'c': print(self.check())
            elif cmd == 'help' or cmd == 'h': self.help()
            # elif cmd == 'debug' : print(self.raport(self.create_db()))
            else: print("Invalid command. Type 'help' or 'h' for more information")
        else: print("Invalid command. Type 'help' or 'h' for more information")

if __name__ == "__main__":
    ids = Ids()
    ids.main()