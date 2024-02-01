import os

def get_size(file):
    if os.path.exists(file):
        return (os.stat(file)).st_size
    else:
        print(f'le fichier {file} n\'existe pas')

if __name__ == '__main__':
    print(f'{get_size("/home/esinck/devTplinux/test.txt")} octets')
