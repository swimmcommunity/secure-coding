It is common for web applications to redirect the user to a new page. For example, this often happens after the user successfully signs in - (s)he is redirected to the original page, this time authenticated. This is often done using a parameter in the HTTP request (such as `next`).

> When a web application accepts untrusted input that could cause the web application to redirect the request to a URL contained within untrusted input. By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials. ([Source](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html))

This technique is common in phishing attacks, for example an attacker could redirect a user from a legitimate login form to a fake login form. If the page looks enough like the target site, and tricks the user into believing they mistyped their password, the attacker can convince the user to re-enter their credentials and send them to the attacker.

Here is an example of a malicious redirect URL ([Source](https://security.openstack.org/guidelines/dg_avoid-unvalidated-redirects.html)):
`https://good.com/login.php?next=http://bad.com/phonylogin.php`

# Additional References
* [OWASP - Unvalidated Redirects and Forwards Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
* [Openstack - Unvalidated URL redirect](https://security.openstack.org/guidelines/dg_avoid-unvalidated-redirects.html)