from hashlib import sha256

ROCKYOU_PATH = './rockyou.txt'
VALUES_TO_READ = 10000000


def generate_rainbow_table(wordlist_file=ROCKYOU_PATH):
    """
    >>> table = generate_rainbow_table()
    >>> table['ada0a4563df9cfd1adef06da9d903562766dcf5b37692ff065fa44da27c51dc3']
    b'freerock123456123'
    >>> table['e4ad93ca07acb8d908a3aa41e920ea4f4ef4f26e7f86cf8291c5db289780a5ae']
    b'iloveyou'
    """
    with open(ROCKYOU_PATH, 'rb') as dictionary_file:
        words_list = dictionary_file.readlines()[:VALUES_TO_READ]
        return {sha256(word.strip()).hexdigest(): word.strip() for word in words_list}
