import itertools
from hashlib import sha256


def bruteforce_generator(characters, min_length, max_length):
    """
    Yield all possible combinations of characters from `characters`, in all string lengths between `min_length` and `max_length`.

    >>> my_generator = bruteforce_generator('abc', 1, 4)
    >>> list(my_generator)
    ['a', 'b', 'c', 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc', 'aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc', 'aaaa', 'aaab', 'aaac', 'aaba', 'aabb', 'aabc', 'aaca', 'aacb', 'aacc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accb', 'accc', 'baaa', 'baab', 'baac', 'baba', 'babb', 'babc', 'baca', 'bacb', 'bacc', 'bbaa', 'bbab', 'bbac', 'bbba', 'bbbb', 'bbbc', 'bbca', 'bbcb', 'bbcc', 'bcaa', 'bcab', 'bcac', 'bcba', 'bcbb', 'bcbc', 'bcca', 'bccb', 'bccc', 'caaa', 'caab', 'caac', 'caba', 'cabb', 'cabc', 'caca', 'cacb', 'cacc', 'cbaa', 'cbab', 'cbac', 'cbba', 'cbbb', 'cbbc', 'cbca', 'cbcb', 'cbcc', 'ccaa', 'ccab', 'ccac', 'ccba', 'ccbb', 'ccbc', 'ccca', 'cccb', 'cccc']
    """
    for length in range(min_length, max_length + 1):
        product = itertools.product(characters, repeat=length)
        for current in product:
            yield ''.join(current)


def is_password(password):
    return sha256(password.encode()).hexdigest() == 'e08bafb3014149296f0154c79215eff5d7c004849cb4ae5b4d329b4c6e018ea5'


def my_bruteforce():
    generator = bruteforce_generator('abcdefg', 1, 8)
    for current_password in generator:
        if is_password(current_password):
            print(f'The right password is {current_password}')
            return

    print("The password was not found")
