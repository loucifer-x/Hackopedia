# Valenfind
**My Dearest Hacker,**

**There’s this new dating app called “Valenfind” that just popped up out of nowhere. I hear the creator only learned to code this year; surely this must be vibe-coded. Can you exploit it?**
*The part where it says "I hear the creator only learned to code this year; surely this must be vibe-coded" is very intresting,it could be a hint towards cross site scripting or SLQ injection.*


## reconnaissance

gobuster dir -w directory-list-2.3-medium.txt -u http://10.129.165.53:5000/
login, register, logout, dashboard, my_profile


nmap -sS -sV 10.129.165.53
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
5000/tcp open  http    Werkzeug httpd 3.0.1 (Python 3.12.3)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
