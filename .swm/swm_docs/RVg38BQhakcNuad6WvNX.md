> A path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files. It should be noted that access to files is limited by system operational access control (such as in the case of locked or in-use files on the Microsoft Windows operating system). ([Source](https://owasp.org/www-community/attacks/Path_Traversal))

This attack has many names, and it is also known as “dot-dot-slash”, “directory traversal”, “directory climbing” and “backtracking”.

## `..`

The attack usually relies on the fact that `..` leads to the "parent directory".
That is, if you have the following paths in your system:
* `/folder_1/aaa/a.txt`
* `/folder_1/bbb/b.txt`

Then `folder_1/aaa/..` is equivalent to `folder_1`. Thus, the following route:

`/folder_1/aaa/../bbb/b.txt` is equivalent to `/folder_1/bbb/b.txt`.

# Example
([Source](https://en.wikipedia.org/wiki/Directory_traversal_attack#Example))

Look at the following vulnerable PHP application:

```
<?php
$template = 'red.php';
if (isset($_COOKIE['TEMPLATE'])) {
    $template = $_COOKIE['TEMPLATE'];
}
include "/home/users/phpguru/templates/" . $template;
```

An attack against this system could be to send the following HTTP request:
```
GET /vulnerable.php HTTP/1.0
Cookie: TEMPLATE=../../../../../../../../../etc/passwd
```

The server would then generate a response such as:

```
HTTP/1.0 200 OK
Content-Type: text/html
Server: Apache

root:fi3sED95ibqR6:0:1:System Operator:/:/bin/ksh 
daemon:*:1:1::/tmp: 
phpguru:f8fk3j1OIf31.:182:100:Developer:/home/users/phpguru/:/bin/csh
```

The repeated `../` characters after `/home/users/phpguru/templates/` have caused `include()` to traverse to the root directory, and then include the Unix password file `/etc/passwd`.


# Additional References
* [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
* [Wikipedia - Directory traversal attack](https://en.wikipedia.org/wiki/Directory_traversal_attack#Example)
* [See the OWASP Testing Guide article on how to test for path traversal vulnerabilities](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.md)