import os
from get.timestamp_to_dico import timestamp_to_dico

def get_timestamp_creation_time(file):
    if os.path.exists(file):
        stat_info = os.stat(file)
        try:
            return stat_info.st_birthtime
        except AttributeError:
            return stat_info.st_ctime
    else :
        print(f'Le fichier {file} n\'existe pas')
        return None

if __name__ == '__main__':
    print(timestamp_to_dico(get_timestamp_creation_time("/home/esinck/devTplinux/ids.py")))
