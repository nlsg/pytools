let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/py/pytools/mpvd/web_ui
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd ~/py/pytools/mpvd
edit ~/py/pytools/mpvd/mpvd.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd w
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
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
exe '1resize ' . ((&lines * 18 + 28) / 57)
exe 'vert 1resize ' . ((&columns * 79 + 79) / 158)
exe '2resize ' . ((&lines * 18 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 78 + 79) / 158)
exe '3resize ' . ((&lines * 36 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 78 + 79) / 158)
exe '4resize ' . ((&lines * 17 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 79 + 79) / 158)
exe '5resize ' . ((&lines * 18 + 28) / 57)
exe 'vert 5resize ' . ((&columns * 79 + 79) / 158)
argglobal
balt ~/py/pytools/mpvd/flaskblog.py
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
21
normal! zo
27
normal! zo
34
normal! zo
38
normal! zo
50
normal! zo
127
normal! zo
let s:l = 129 - ((52 * winheight(0) + 9) / 18)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 129
normal! 0
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("~/py/pytools/mpvd/web_ui/flaskblog.py") | buffer ~/py/pytools/mpvd/web_ui/flaskblog.py | else | edit ~/py/pytools/mpvd/web_ui/flaskblog.py | endif
if &buftype ==# 'terminal'
  silent file ~/py/pytools/mpvd/web_ui/flaskblog.py
endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
106
normal! zo
110
normal! zo
111
normal! zo
let s:l = 114 - ((11 * winheight(0) + 9) / 18)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 114
normal! 0
lcd ~/py/pytools/mpvd/web_ui
wincmd w
argglobal
if bufexists("term://~/py/pytools/mpvd//1842:/bin/bash") | buffer term://~/py/pytools/mpvd//1842:/bin/bash | else | edit term://~/py/pytools/mpvd//1842:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/py/pytools/mpvd//1842:/bin/bash
endif
balt ~/py/pytools/mpvd/mpvd.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 579 - ((35 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 579
normal! 0
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("~/py/pytools/mpvd/run.sh") | buffer ~/py/pytools/mpvd/run.sh | else | edit ~/py/pytools/mpvd/run.sh | endif
if &buftype ==# 'terminal'
  silent file ~/py/pytools/mpvd/run.sh
endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 4 - ((2 * winheight(0) + 8) / 17)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 05|
lcd ~/py/pytools/mpvd
wincmd w
argglobal
if bufexists("~/py/pytools/mpvd/run.py") | buffer ~/py/pytools/mpvd/run.py | else | edit ~/py/pytools/mpvd/run.py | endif
if &buftype ==# 'terminal'
  silent file ~/py/pytools/mpvd/run.py
endif
balt term://~/py/pytools/mpvd//14252:/bin/bash
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
3
normal! zo
5
normal! zo
11
normal! zo
15
normal! zo
19
normal! zo
let s:l = 20 - ((9 * winheight(0) + 9) / 18)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 20
normal! 09|
lcd ~/py/pytools/mpvd
wincmd w
5wincmd w
exe '1resize ' . ((&lines * 18 + 28) / 57)
exe 'vert 1resize ' . ((&columns * 79 + 79) / 158)
exe '2resize ' . ((&lines * 18 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 78 + 79) / 158)
exe '3resize ' . ((&lines * 36 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 78 + 79) / 158)
exe '4resize ' . ((&lines * 17 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 79 + 79) / 158)
exe '5resize ' . ((&lines * 18 + 28) / 57)
exe 'vert 5resize ' . ((&columns * 79 + 79) / 158)
tabnext 1
badd +127 ~/py/pytools/mpvd/mpvd.py
badd +0 ~/py/pytools/mpvd/flaskblog.py
badd +0 ~/py/pytools/mpvd/check_pids.sh
badd +114 ~/py/pytools/mpvd/web_ui/flaskblog.py
badd +1 ~/py/pytools/mpvd/launch_server.sh
badd +11 term://~/py/pytools/mpvd//82635:/bin/bash
badd +10 term://~/py/pytools/mpvd//26056:/bin/bash
badd +2 term://~/py/pytools/mpvd//15848:/bin/bash
badd +27 term://~/py/pytools/mpvd//16758:/bin/bash
badd +116 ~/py/batd/daemon_class.py
badd +1 ~/py/pytools/mpvd/mpvd.log
badd +2 term://~/py/pytools/mpvd//1554306:/bin/bash
badd +1 ~/py/batd/batd.py
badd +2 ~/py/pytools/mpvd/nohup.out
badd +28 ~/py/pytools/mpvd/mpvlauncher.py
badd +1 ~/sys_cfg/open_mpv.pysf
badd +11 ~/sys_cfg/open_mpv.py
badd +2 term://~/py/pytools/mpvd//3308106:/bin/bash
badd +1 ~/tmp.sh
badd +2 term://~/py/pytools/mpvd/web_ui//3405646:/bin/bash
badd +52 ~/py/pytools/mpvd/web_ui/templates/login.html
badd +1 ~/py/pytools/mpvd/web_ui/templates/layout.html
badd +2 term://~/py/pytools/mpvd/web_ui//3424386:/bin/bash
badd +13 ~/py/turbo_flask_examples/load/templates/base.html
badd +1 ~/py/turbo_flask_examples/load/templates/index.html
badd +57 ~/py/Flask_Blog/03-Forms-and-Validation/flaskblog.py
badd +2 term://~/py/pytools/mpvd/web_ui//3572653:/bin/bash
badd +74 term://~/py/pytools/mpvd//1842:/bin/bash
badd +2 term://~/py/pytools/mpvd//3236:/bin/bash
badd +11 ~/py/pytools/mpvd/run.sh
badd +2 term://~/py/pytools/mpvd//14252:/bin/bash
badd +17 ~/py/pytools/mpvd/run.py
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
