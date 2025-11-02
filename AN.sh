#!/data/data/com.termux/files/usr/bin/bash
echo "alias ANTOOL='cd $HOME/ANTOOL && chmod +x AN && ./AN'" >> $HOME/.bashrc
echo "工具安装成功,下次启动直接输入[ANTOOL]即可进入工具"
source ~/.bashrc