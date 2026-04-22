# Valenfind
**My Dearest Hacker,**

**There’s this new dating app called “Valenfind” that just popped up out of nowhere. I hear the creator only learned to code this year; surely this must be vibe-coded. Can you exploit it?**
*The part where it says "I hear the creator only learned to code this year; surely this must be vibe-coded" is very intresting,it could be a hint towards cross site scripting or SLQ injection.* 



## reconnaissance

```
gobuster dir -w directory-list-2.3-medium.txt -u http://10.129.165.53:5000/
login, register, logout, dashboard, my_profile
```
```
nmap -sS -sV 10.129.165.53
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
5000/tcp open  http    Werkzeug httpd 3.0.1 (Python 3.12.3)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


While creating an account for this website I decided to try adding an alert script in the bio section to check for XSS exploit.
```
<script>alert("helloworld")</script>
```

After creating a account I notcied I can view other peoples profiles. I decided to make another account and click on the account I just made to see if the script worked. The script was sanatized.

*Theres a lot of accounts registered to this site on /dashboard. Cupid stands out the most since its a cupid website plus the bio states "I keep the database secrure. No peeking" So I assume this is where the flag is placed.*

After this reconnaissance I found nothing intresting so i decide to look into inspect element. 

-  Inspect element | N/A
-  Debugger | N/A
-  NETWORK | ```GET http://10.129.165.53:5000/api/fetch_layout?layout=theme_classic.html```

Looks like there's a possible LFI exploit! Let's start digging, in my notes in web hacking we can use ```../../../../etc/passwd``` to find directories!



  


