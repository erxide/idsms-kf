import hashlib

def gethash_SHA512(file):
	with open(file, 'rb') as f:
		return (hashlib.sha512(f.read())).hexdigest()

if __name__ == '__main__':
	print(gethash_SHA512('/home/esinck/devTplinux/test.txt'))
