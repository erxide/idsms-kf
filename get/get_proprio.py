import os
import pwd

def get_proprio(file):
    if os.path.exists(file):
        return (pwd.getpwuid(os.stat(file).st_uid)).pw_name
    else:
        print(f'le fichier {file} n\'existe pas')

if __name__ == '__main__':
    print(get_proprio('/home/esinck/devTplinux/test.txt'))
