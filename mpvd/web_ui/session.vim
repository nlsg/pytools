let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/py/batd
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd ~/py/pytools/mpvd
set stal=2
tabnew
tabrewind
edit ~/py/pytools/mpvd/web_ui/templates/battery_info.html
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd _ | wincmd |
split
1wincmd k
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
exe '1resize ' . ((&lines * 27 + 28) / 57)
exe 'vert 1resize ' . ((&columns * 74 + 74) / 149)
exe '2resize ' . ((&lines * 26 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 74 + 74) / 149)
exe 'vert 3resize ' . ((&columns * 74 + 74) / 149)
argglobal
balt term://~/py/pytools/mpvd/web_ui/templates//1275884:/bin/bash
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
3
normal! zo
4
normal! zo
5
normal! zo
6
normal! zo
8
normal! zo
let s:l = 4 - ((3 * winheight(0) + 13) / 27)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 024|
lcd ~/py/pytools/mpvd/web_ui/templates
wincmd w
argglobal
if bufexists("~/py/pytools/mpvd/web_ui/templates/battery_plot.html") | buffer ~/py/pytools/mpvd/web_ui/templates/battery_plot.html | else | edit ~/py/pytools/mpvd/web_ui/templates/battery_plot.html | endif
if &buftype ==# 'terminal'
  silent file ~/py/pytools/mpvd/web_ui/templates/battery_plot.html
endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
2
normal! zo
6
normal! zo
8
normal! zo
let s:l = 5 - ((4 * winheight(0) + 13) / 26)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5
normal! 014|
lcd ~/py/pytools/mpvd/web_ui/templates
wincmd w
argglobal
if bufexists("~/py/pytools/mpvd/web_ui/flaskblog.py") | buffer ~/py/pytools/mpvd/web_ui/flaskblog.py | else | edit ~/py/pytools/mpvd/web_ui/flaskblog.py | endif
if &buftype ==# 'terminal'
  silent file ~/py/pytools/mpvd/web_ui/flaskblog.py
endif
balt ~/py/pytools/mpvd/web_ui/templates/plot.html
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
33
normal! zo
42
normal! zo
43
normal! zo
121
normal! zo
125
normal! zo
136
normal! zo
136
normal! zc
let s:l = 59 - ((45 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 59
normal! 07|
lcd ~/py/pytools/mpvd/web_ui
wincmd w
3wincmd w
exe '1resize ' . ((&lines * 27 + 28) / 57)
exe 'vert 1resize ' . ((&columns * 74 + 74) / 149)
exe '2resize ' . ((&lines * 26 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 74 + 74) / 149)
exe 'vert 3resize ' . ((&columns * 74 + 74) / 149)
tabnext
edit ~/py/batd/batd.py
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
16
normal! zo
30
normal! zo
66
normal! zo
let s:l = 43 - ((42 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 43
normal! 035|
lcd ~/py/batd
tabnext 1
set stal=1
badd +1 ~/py/pytools/mpvd
badd +63 ~/py/pytools/mpvd/mpvd.py
badd +0 ~/py/pytools/mpvd/flaskblog.py
badd +49 ~/py/pytools/mpvd/web_ui/flaskblog.py
badd +18 ~/py/pytools/mpvd/run.py
badd +0 term://~/py/pytools/mpvd//14252:/bin/bash
badd +1 ~/py/pytools/mpvd/check_pids.sh
badd +1 ~/py/pytools/mpvd/launch_server.sh
badd +11 term://~/py/pytools/mpvd//82635:/bin/bash
badd +10 term://~/py/pytools/mpvd//26056:/bin/bash
badd +2 term://~/py/pytools/mpvd//15848:/bin/bash
badd +27 term://~/py/pytools/mpvd//16758:/bin/bash
badd +116 ~/py/batd/daemon_class.py
badd +1 ~/py/pytools/mpvd/mpvd.log
badd +2 term://~/py/pytools/mpvd//1554306:/bin/bash
badd +47 ~/py/batd/batd.py
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
badd +2 term://~/py/pytools/mpvd//3236:/bin/bash
badd +11 ~/py/pytools/mpvd/web_ui/templates/notdash.html
badd +2 term://~/py/batd//580367:/bin/bash
badd +11 ~/py/batd/_batd.ini
badd +5 ~/py/pytools/mpvd/web_ui/templates/plot.html
badd +2 ~/py/pytools/mpvd/web_ui/templates/battery_plot.html
badd +3 term://~/py/pytools/mpvd/web_ui/templates//1275884:/bin/bash
badd +2 term://~/py/pytools/mpvd/web_ui/templates//1280495:/bin/bash
badd +12 ~/py/pytools/mpvd/web_ui/templates/battery_info.html
badd +2 term://~/py/pytools/mpvd/web_ui/templates//1318837:/bin/bash
badd +2 term://~/py/pytools/mpvd/web_ui/templates//1322450:/bin/bash
badd +9 ~/py/pytools/mpvd/web_ui/templates/dyn_board.html
badd +2 term://~/py/pytools/mpvd/web_ui/templates//1600091:/bin/bash
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOF
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
