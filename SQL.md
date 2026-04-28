**Commands**

SHOW TABLES;


**Notes**

Anything after -- on the same line is ignored by the database.
```https://gchq.github.io/CyberChef/``` to encode URLS


**Filter Evasion Techniques**

*  **URL Encoding** - Common encoding method where characters are represetned using **%** followed by their ASCII value. ```' OR 1=1--``` -> ```%27%20OR%201%3D1--```

*  **Hexadecimal Encoding** - ```SELECT * FROM users WHERE name = 'admin'``` -> ```SELECT * FROM users WHERE name = 0x61646d696e```  

*  **Unicode Encoding** -  ```admin``` -> ```\u0061\u0064\u006d\u0069\u006e``` Bypass filters that only check for specific ASCII characters.

