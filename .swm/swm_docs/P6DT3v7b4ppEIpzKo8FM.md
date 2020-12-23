When we write code, we may want to interact with the operating system. This happens very often - for example when we write a file, read data from the network, or using an external process. 

> Command Injection is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application. Command injection attacks are possible when an application passes unsafe user supplied data (forms, cookies, HTTP headers etc.) to a system shell. In this attack, the attacker-supplied operating system commands are usually executed with the privileges of the vulnerable application. Command injection attacks are possible largely due to insufficient input validation. ([Source](https://owasp.org/www-community/attacks/Command_Injection))

Specifically, shelling out to another program is a pretty common thing to want to do - and it is often vulnerable to Command Injection.

# An example ([Source](https://owasp.org/www-community/attacks/Command_Injection))
The following PHP code snippet is vulnerable to a command injection attack:

```
<?php
print("Please specify the name of the file to delete");
print("<p>");
$file=$_GET['filename'];
system("rm $file");
?>
```

The following request and response is an example of a successful attack:

## Request
`http://127.0.0.1/delete.php?filename=bob.txt;id`

## Response
```Please specify the name of the file to delete

uid=33(www-data) gid=33(www-data) groups=33(www-data)```

## Explanation
By using `bob.txt;id` as the `filename`, the attacker was able to launch the following command:
`system("rm bob.txt;id");`

This is the equivalent of running `rm bob.txt` and then running `id`. This way the attacker was able to get the sensitive data from the `id` command.

# Additional References
* [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)