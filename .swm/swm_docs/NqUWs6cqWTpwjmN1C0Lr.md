> Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

> An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page. ([Source](https://owasp.org/www-community/attacks/xss/))

# Example ([Source](https://owasp.org/www-community/attacks/xss/))
Let’s assume that we have an error page, which is handling requests for non existing pages - a classic 404 error page. We may use the code below as an example to inform user about what specific page is missing:

```
<html>
<body>
<? php
print "Not found: " . urldecode($_SERVER["REQUEST_URI"]);
?>

</body>
</html>
```

If a user issues a request to `http://testsite.test/file_which_not_exist`, (s)he will receive in response: `Not found: /file_which_not_exist`

An attacker can force the error page to include her code by issuing: 

`http://testsite.test/<script>alert("TEST");</script>`

The result is:
`Not found: / (but with JavaScript code <script>alert("TEST");</script>)`


# Additional References
* [OWASP - https://owasp.org/www-community/attacks/xss/](https://owasp.org/www-community/attacks/xss/)
* [OWASP’s XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)