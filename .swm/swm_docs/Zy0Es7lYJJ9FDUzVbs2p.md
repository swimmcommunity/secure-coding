Passwords should never be stored as plaintext. Ever.

This guideline is very clear. If a password is stored as plaintext, and the database storing this password is compromised - the person gaining access to this database will know the password.

# What are hashes?
Passwords are typically *hashed* with a one-way hashing function. This is a mathematical operation that's easy to perform, yet difficult to reverse. Like other forms of encryption, it turns readable data (*plaintext*) into a scrambled cipher. The difference from other encryption forms is that the goal with hashing is not to allow someone to decrypt the data if they have the right key. Hashes aren't designed to be decrypted. Instead, when you authenticate using a password, the remote service will perform that function again and check your result.

There are many hash functions, among the common ones nowadays are `SHA256`, `SHA512`, `Argon2`, `PBKDF2` and `Bcrypt`.

For example, say that you registered to a service with the username `my_user` and the password `hello_world`. The `SHA256` hash of this password is `35072c1ae546350e0bfa7ab11d49dc6f129e72ccd57ec7eb671225bbd197c8f1`.

A service that stores the SHA256 form of passwords (instead of plaintext) will store that the user `my_user` has the password with the hash of `35072c1ae546350e0bfa7ab11d49dc6f129e72ccd57ec7eb671225bbd197c8f1`.

Now, say someone attemps to login with the wrong password - for example `wrong_password`. The remote service then computes `sha256('wrong_password')` and gets the value `8b6308341eeeab569dc420933ecd4d955b4ed3ade17eafa650f011e93acb434f`. Since this value is different than the stored one - access is not granted.

Then, if you try to login with the password `hello_world`, the service performs `sha256('hello_world')`. Since the result matches the stored value - access is indeed granted.

# Are hashes safe?
Well, if a password is hashed, will it mean that you can't break it?

We will consider this question in the following Unit(s).

# Additional references
* [OWASP - Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)