import hashlib

def gethash_MD5(file):
        with open(file, 'rb') as f:
                return (hashlib.md5(f.read())).hexdigest()

if __name__ == '__main__':
        print(gethash_MD5('/home/esinck/devTplinux/test.txt'))
