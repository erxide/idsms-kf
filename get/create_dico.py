from get.gethash_SHA256 import gethash_SHA256
from get.gethash_SHA512 import gethash_SHA512
from get.gethash_MD5 import gethash_MD5
from get.get_timestamp_lastmodif_time import get_timestamp_lastmodif_time
from get.get_timestamp_creation_time import get_timestamp_creation_time
from get.get_proprio import get_proprio
from get.get_groups import get_groups
from get.get_size import get_size

def create_dico(file):
    data = {
        'hash': {
            'SHA256': gethash_SHA256(file),
            'SHA512': gethash_SHA512(file),
            'MD5': gethash_MD5(file)
        },
        'lastmodif': get_timestamp_lastmodif_time(file),
        'creation': get_timestamp_creation_time(file),
        'proprio': get_proprio(file),
        'groups': get_groups(file),
        'size': get_size(file)
    }

    return data

if __name__ == '__main__':
    print(create_dico('test.txt'))
