from hashlib import sha256

from simple_bruteforce import bruteforce_generator


def my_bruteforce(hash_to_break):
    """
    This function receives a sha-256 hash `hash_to_break` and returns its corresponding plaintext password.
    Assumptions about the corresponding password:
    * The password consists of 1-8 characters
    * Each character is from `abcdefg`
    
    >>> my_bruteforce('e124adcce1fb2f88e1ea799c3d0820845ed343e6c739e54131fcb3a56e4bc1bd')
    'aba'
    >>> my_bruteforce('e08bafb3014149296f0154c79215eff5d7c004849cb4ae5b4d329b4c6e018ea5')
    'ebdgafba'
    """
    generator = bruteforce_generator('abcdefg', 1, 8)
    for current_password in generator:
        if sha256(current_password.encode()).hexdigest() == hash_to_break:
            return current_password

    print("The password was not found")
