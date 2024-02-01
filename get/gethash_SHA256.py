import hashlib

def gethash_SHA256(file):
        with open(file, 'rb') as f:
                return (hashlib.sha256(f.read())).hexdigest()

if __name__ == "__main__":
        file = "/home/esinck/devTplinux/test.txt"
        print(gethash_SHA256(file))
