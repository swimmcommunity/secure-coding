As we've seen, it's relatively easy to crack a hash if the attacker knows the hashing algorithm, and if the password is included in a password list or can be quickly bruteforced.

However, this process can take time. Consider your implementation of a dictionary attack - you had to go over the entire dictionary, and compute the hash for each of its values - every single time!

That isn't so efficient, is it?

To make things shorter, attackers can rely on **Rainbow Tables**. From [Wikipedia](https://en.wikipedia.org/wiki/Rainbow_table):
> A rainbow table is a precomputed table for caching the output of cryptographic hash functions, usually for cracking password hashes. 

# Additional Resources
* [Wikipedia - Rainbow Table](https://en.wikipedia.org/wiki/Rainbow_table)