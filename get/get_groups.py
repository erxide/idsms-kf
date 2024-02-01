import os
import grp

def get_groups(file):
    if os.path.exists(file):
        return grp.getgrgid(os.stat(file).st_gid).gr_name
    else:
        print(f'le fichier {file} n\'existe pas')
if __name__ == '__main__':
    print(get_groups('/home/esinck/devTplinux/test.txt'))

