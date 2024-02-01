import os
from get.timestamp_to_dico import timestamp_to_dico

def get_timestamp_lastmodif_time(file):
    if os.path.exists(file):
        stat_info = os.stat(file)
        return stat_info.st_mtime
    else :
        print(f'Le fichier {file} n\'existe pas')
        return None

if __name__ == '__main__':
    print(timestamp_to_dico(get_timestamp_lastmodif_time("//home/esinck/devTplinux/test.txt")))
