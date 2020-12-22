Bruteforce attacks can take time, even a lot of time, given a long password that can consist of many different characters.

Attackers can also rely on the fact that most humans don't just use a random sequence of characters for their passwords.

For a bruteforce attack, both of these options are quite similar:
(1) `newpassword`
(2) `mldpsaiorld`

They both consist of the same number of characters. Actually, since the second password starts with `m`, which usually comes before `n`, a bruteforce attack will probably make less attempts in order to guess `(2)`.

However, the first password is used much more frequently than the second.

There are many lists of frequently used passwords available online, and attackers use them in order to guess passwords. One famous list is called `rockyou`, and you can download it [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).