## No SQL
*Instead of using traditional SQL syntax (like in SQL injection), NoSQL injection targets query formats such as JSON, JavaScript objects, or query operators. Databases such as MongoDB
Apache, CouchDB, Couchbase, Amazon DocumentDB may be susceptible to NoSql injection.


**different payloads** *PUT REQUEST*
-  ```username[$ne]=user123&password[$ne]=pass123``` - *Forces a match for any user whose username is NOT user123 AND password is NOT pass123* Stackable ->```username[$ne]=user123&username[$ne]=user123&```
