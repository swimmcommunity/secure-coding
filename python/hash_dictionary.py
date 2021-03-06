from hashlib import sha256

ROCKYOU_PATH = './rockyou.txt'


def dictionary_attack(sha256_hash_to_break):
    """
    >>> dictionary_attack('ada0a4563df9cfd1adef06da9d903562766dcf5b37692ff065fa44da27c51dc3')
    b'freerock123456123'
    >>> dictionary_attack('e4ad93ca07acb8d908a3aa41e920ea4f4ef4f26e7f86cf8291c5db289780a5ae')
    b'iloveyou'
    """
    with open(ROCKYOU_PATH, 'rb') as dictionary_file:
        words_list = dictionary_file.readlines()
        for word in words_list:
            word = word.strip()
            if sha256(word).hexdigest() == sha256_hash_to_break:
                return word

    print("The password was not found")
