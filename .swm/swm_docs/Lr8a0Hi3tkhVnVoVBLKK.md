As we've seen, it's relatively easy to crack a hash if the attacker knows the hashing algorithm, and if the password is included in a password list or can be quickly bruteforced.

However, this process can take time. Consider your implementation of a dictionary attack - you had to go over the entire dictionary, and compute the hash for each of its values - every single time!

That isn't so efficient, is it?

To make things shorter, attackers can rely on **Lookup Tables**. From [Crackstation - Hashing Security](https://crackstation.net/hashing-security.htm):
> The general idea is to pre-compute the hashes of the passwords in a password dictionary and store them, and their corresponding password, in a lookup table data structure. A good implementation of a lookup table can process hundreds of hash lookups per second, even when they contain many billions of hashes.