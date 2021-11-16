# pytools
this is basically my "sketchbook" folder
most of the scripts don't fulfill a purpose,
they are just tests, modified examples 

## nls_util.py
this is my personal "misc-library" of general purpose functions,
most of the time i tend to import it like so..
```import nls_util as nut```

it includes:
 - decorators
 - utility functions
 - a dict called cli, it contains terminal midifiers like "BOLD" and so on..

## push.py
A simple tool to automate the git push process.
It generates a "push.ini" file for each repository,
all options in its "chain" section get executed 
as shell command, before the "git commit -m"  command" does.
in the "push" section are a few self explanatory options.
If you dont want mandatory commit messages:

```request_msg = 0
   pre_msg = "standard message"
```
