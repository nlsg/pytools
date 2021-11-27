# pytools
this is basically my "sketchbook" folder
most of the scripts don't fulfill a purpose,
they are just tests, modified examples 

# nls_util.py
this is my personal "misc-library" of general purpose functions,
most of the time i tend to import it like so..
```import nls_util as nut```

it includes:
 - decorators
 - utility functions
 - a dict called cli, it contains terminal midifiers like "BOLD" and so on..

# push.py
A simple tool to automate the git push process.
It generates a "push.ini" file for each repository,
all options in its "chain" section get executed 
as shell command, before the "git commit -m"  command" does.

usage:
------
option -m and -i are combinable
```
push.py (-i <ini-file>) [no_arg] | -m <msg> | -v[iew] <file> | -a[dd cmd] <cmd> | -h
```

In the "push" section are a few self explanatory options.
If you dont want to write a message for every commit,
set the default_msg variable

```[push]
pre_msg = 
post_msg = 
default_msg = minor updates
repository = pytools
branch =
confirm_before_push = True
 
[chain]
cmd0 = git add .
cmd1 = git status
cmd2 = ls | grep py
cmdxy = git branch
. . .
```
