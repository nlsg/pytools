let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/py/pytools/mpvd
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd ~/py/pytools/mpvd
edit mpvd.py
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
wincmd _ | wincmd |
split
4wincmd k
wincmd w
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
exe '2resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 106 + 106) / 212)
exe '3resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 106 + 106) / 212)
exe '4resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 106 + 106) / 212)
exe '5resize ' . ((&lines * 11 + 28) / 57)
exe 'vert 5resize ' . ((&columns * 106 + 106) / 212)
exe '6resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 6resize ' . ((&columns * 106 + 106) / 212)
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
12
normal! zo
13
normal! zo
17
normal! zo
18
normal! zo
21
normal! zo
22
normal! zo
27
normal! zo
28
normal! zo
33
normal! zo
36
normal! zo
37
normal! zo
43
normal! zo
44
normal! zo
47
normal! zo
48
normal! zo
57
normal! zo
58
normal! zo
59
normal! zo
64
normal! zo
72
normal! zo
80
normal! zo
85
normal! zo
94
normal! zo
98
normal! zo
103
normal! zo
let s:l = 75 - ((44 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 75
normal! 05|
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("term://~/py/pytools/mpvd//1497729:/bin/bash") | buffer term://~/py/pytools/mpvd//1497729:/bin/bash | else | edit term://~/py/pytools/mpvd//1497729:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools/mpvd//1497729:/bin/bash
endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 10 - ((9 * winheight(0) + 5) / 10)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 10
normal! 0
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("term://~/py/pytools/mpvd//1505542:/bin/bash") | buffer term://~/py/pytools/mpvd//1505542:/bin/bash | else | edit term://~/py/pytools/mpvd//1505542:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools/mpvd//1505542:/bin/bash
endif
balt term://~/py/pytools/mpvd//1497729:/bin/bash
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 10 - ((9 * winheight(0) + 5) / 10)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 10
normal! 0
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("~/py/pytools/mpvd/launch_server.sh") | buffer ~/py/pytools/mpvd/launch_server.sh | else | edit ~/py/pytools/mpvd/launch_server.sh | endif
if &buftype ==# 'terminal'
  silent file ~/py/pytools/mpvd/launch_server.sh
endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 6 - ((5 * winheight(0) + 5) / 10)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 6
normal! 0
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("term://~/py/pytools/mpvd//82635:/bin/bash") | buffer term://~/py/pytools/mpvd//82635:/bin/bash | else | edit term://~/py/pytools/mpvd//82635:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools/mpvd//82635:/bin/bash
endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((3 * winheight(0) + 5) / 11)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5
normal! 0
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("term://~/py/pytools/mpvd//26056:/bin/bash") | buffer term://~/py/pytools/mpvd//26056:/bin/bash | else | edit term://~/py/pytools/mpvd//26056:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools/mpvd//26056:/bin/bash
endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5741 - ((0 * winheight(0) + 5) / 10)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5741
normal! 017|
lcd ~/py/pytools/mpvd
wincmd w
exe 'vert 1resize ' . ((&columns * 105 + 106) / 212)
exe '2resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 106 + 106) / 212)
exe '3resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 106 + 106) / 212)
exe '4resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 106 + 106) / 212)
exe '5resize ' . ((&lines * 11 + 28) / 57)
exe 'vert 5resize ' . ((&columns * 106 + 106) / 212)
exe '6resize ' . ((&lines * 10 + 28) / 57)
exe 'vert 6resize ' . ((&columns * 106 + 106) / 212)
tabnext 1
badd +73 ~/py/pytools/mpvd/mpvd.py
badd +2 term://~/py/pytools/mpvd//15848:/bin/bash
badd +27 term://~/py/pytools/mpvd//16758:/bin/bash
badd +5750 term://~/py/pytools/mpvd//26056:/bin/bash
badd +116 ~/py/batd/daemon_class.py
badd +14 term://~/py/pytools/mpvd//82635:/bin/bash
badd +3 ~/py/pytools/mpvd/launch_server.sh
badd +1 ~/py/pytools/mpvd/mpvd.log
badd +13 term://~/py/pytools/mpvd//1497729:/bin/bash
badd +0 term://~/py/pytools/mpvd//1505542:/bin/bash
badd +2 term://~/py/pytools/mpvd//1554306:/bin/bash
badd +0 ~/py/batd/batd.py
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOF
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
