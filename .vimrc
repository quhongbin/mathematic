call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree'
Plug 'vim-airline/vim-airline'
call plug#end()
map <F2> :NERDTreeToggle<CR>

imap jk <Esc>
nmap <Space> :


set nu "显示作侧行
"切换窗口
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l
