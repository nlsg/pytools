let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd py/pytools/cheatsheet.hy
edit py/pytools/cheatsheet.hy
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
3wincmd k
wincmd w
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 105 + 106) / 212)
exe '2resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 106 + 106) / 212)
exe '3resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 106 + 106) / 212)
exe '4resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 106 + 106) / 212)
exe '5resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 5resize ' . ((&columns * 106 + 106) / 212)
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
8
normal! zo
10
normal! zo
11
normal! zo
11
normal! zo
11
normal! zo
19
normal! zo
21
normal! zo
30
normal! zo
33
normal! zo
33
normal! zo
33
normal! zo
33
normal! zo
33
normal! zo
33
normal! zo
33
normal! zo
33
normal! zo
33
normal! zo
39
normal! zo
39
normal! zo
let s:l = 22 - ((21 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 22
normal! 03|
lcd ~/py/pytools
wincmd w
argglobal
if bufexists("~/py/pytools/cheatsheet.py") | buffer ~/py/pytools/cheatsheet.py | else | edit ~/py/pytools/cheatsheet.py | endif
if &buftype ==# 'terminal'
  silent file ~/py/pytools/cheatsheet.py
endif
balt term://~/py/pytools//57906:/bin/bash
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
2
normal! zo
7
normal! zo
let s:l = 6 - ((1 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 6
normal! 0
lcd ~/py/pytools
wincmd w
argglobal
if bufexists("term://~/py/pytools//62067:/bin/bash") | buffer term://~/py/pytools//62067:/bin/bash | else | edit term://~/py/pytools//62067:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools//62067:/bin/bash
endif
balt ~/py/pytools/cheatsheet.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 13 - ((12 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 0
lcd ~/py/pytools
wincmd w
argglobal
if bufexists("term://~/py/pytools//61951:/bin/bash") | buffer term://~/py/pytools//61951:/bin/bash | else | edit term://~/py/pytools//61951:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools//61951:/bin/bash
endif
balt ~/py/pytools/cheatsheet.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 13 - ((12 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 0
lcd ~/py/pytools
wincmd w
argglobal
if bufexists("term://~/py/pytools//60483:/bin/bash") | buffer term://~/py/pytools//60483:/bin/bash | else | edit term://~/py/pytools//60483:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools//60483:/bin/bash
endif
balt ~/py/pytools/cheatsheet.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 13 - ((12 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 0
lcd ~/py/pytools
wincmd w
exe 'vert 1resize ' . ((&columns * 105 + 106) / 212)
exe '2resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 106 + 106) / 212)
exe '3resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 106 + 106) / 212)
exe '4resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 106 + 106) / 212)
exe '5resize ' . ((&lines * 13 + 28) / 57)
exe 'vert 5resize ' . ((&columns * 106 + 106) / 212)
tabnext 1
badd +25 ~/py/pytools/cheatsheet.hy
badd +27 term://~/py/pytools//57906:/bin/bash
badd +6 ~/py/pytools/cheatsheet.py
badd +0 term://~/py/pytools//60483:/bin/bash
badd +0 term://~/py/pytools//61951:/bin/bash
badd +0 term://~/py/pytools//62067:/bin/bash
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOFc
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
