import random
import string
from hashlib import sha256


def register_user(database, username, password):
    """
    Regsiters the username to the database.
    The database has the format of:
    {username: (hashed_value, salt)}

    >>> my_database = {}
    >>> register_user(my_database, b'swimm_user', b'swimm_password')
    >>> register_user(my_database, b'swimm_user', b'another_password')
    False
    >>> register_user(my_database, b'another_user', b'swimm_password')
    >>> my_database[b'swimm_user'][0] == my_database[b'another_user'][0]
    False
    """
    if username in database:
        # This user already exists
        return False

    salt = get_random_salt()
    hashed_value = sha256(password+salt).hexdigest()
    database[username] = (hashed_value, salt)


def get_random_salt(size=8):
    return ''.join(random.choices(string.ascii_letters, k=size)).encode()


def login(database, username, password):
    """
    Returns True if the user exists in the DB and used the right password to login.
    Returns False otherwise.

    >>> my_database = {}
    >>> register_user(my_database, b'swimm_user', b'swimm_password')
    >>> register_user(my_database, b'another_user', b'swimm_password')
    >>> login(my_database, b'non_existing_user', b'swimm_password')
    False
    >>> login(my_database, b'swimm_user', b'wrong_password')
    False
    >>> login(my_database, b'swimm_user', b'swimm_password')
    True
    """
    if username not in database:
        return False

    (hashed_password, salt) = database[username]
    return sha256(password+salt).hexdigest() == hashed_password
