from colorama import Fore, init
from time import sleep
import sys

init(autoreset=True)

def tfGenerator():
    while True:
        yield from [True] * 3
        yield from [False] * 15
it = tfGenerator()

def delayPrint(s, color=None) -> None:
    for c in s:
        if color == 'green':
            print(Fore.GREEN + c, end='')
        elif color == 'cyan':
            print(Fore.CYAN + c, end='')
        elif color == 'red':
            print(Fore.RED + c, end='')
        elif color == 'yellow':
            print(Fore.YELLOW + c, end='')
        else:
            print(Fore.RESET + c, end='')
        sys.stdout.flush()
        if next(it):
            sleep(0.02)

# Dynamic bar:
def dynamicBar() -> None:
    i = 0
    bar = '* * * * * * * * * * * * * * *'
    while True:
        sleep(0.2)
        if bar[i] != ' ':
            # Move cursor up 
            print('\033[16F' + Fore.CYAN + '           {0}'.format(bar[:i] + ' ' + bar[i+1:]))
            # Move cursor back 
            print(f'\033[16E', end='')
        i = (i+1) % len(bar)

# Line 1
delayPrint('\n歡迎光臨  ')
delayPrint('5525 回到那一天  ', 'red')
delayPrint('（目前共有 ')
delayPrint('55255 ', 'cyan')
delayPrint('人上線）\n')

# Line 2
delayPrint('請輸入代號（試用請輸入 `')
delayPrint('guest', 'cyan')
delayPrint('`，註冊請輸入 `')
delayPrint('new', 'cyan')
delayPrint('`）：mayday\n')

# Line 3 
delayPrint('請輸入密碼：********\n')

# Snow White
delayPrint('         ::::::::::`.d$N.^``...:::db.^`:::::::::::     \n')
delayPrint('        .::::::::: *#` ::::::::`z$$$$$bo.```::::::     \n')
delayPrint('        :::::::``..-:::::::: `u$$$$$$$$$$$$bu `:::     \n')
delayPrint('       ::::::`.::::::::::`.ud$$$$$$$$$$$$$$$$$  :`     \n')
delayPrint('       ::::: ::::::::`.ud$$$$$$$$$$$$$$$$∂eeuJ> :      \n')
delayPrint('     . `::::::::::: xd$$$$R`Lued$$$$$$$$$$$$$$>.:      \n')
delayPrint('   ::::.::::::::::. 9$$$$Fz$$$$$$$$$$$$$$$$F`` .:      \n')
delayPrint('  ::::::::::::::::::`$$$$u$$$F` ``$$$$$$$$.ut  `::     \n')
delayPrint('  :::::::::::::::::::`$$$$$FskxL. 9$$$$$$$edNeo :::    \n')
delayPrint('  :::::::::::::::::::`$$$$$FskxL. 9$$$$$$$edNeo :::    \n')
delayPrint('   `:::::::::::::::::: 4$$$$$b$euud$$$$$$$$$$$$$  : %%%\n')
delayPrint('%: `::: :::::::::::::: $$$$$$$$$$$$$$$$$$?$$$$$>  %%%% \n')
delayPrint('%%%     ::::::::::::: .$$$$$$$$$$$$$$$$I$u$$$$$> %%%%  \n')
delayPrint('%%%%%:  ::::::::::::` d$$$$$$$$$$$$$$$R???`7$$F %%%%   \n')
delayPrint(' %%%%%%  ::::::::::`.$$$$$$$$$$$$$b.-m$$* d$$F %%%`    \n')
delayPrint('   %%%%%.  :::::::: t$$$$$$$$$$$$$$$bu..o$$$`.%%       \n')
delayPrint('    `%%%%%%.   :::: `$$$$$$$$$$$$$$$$$$$$$F`:%%        \n')
delayPrint('    `s.`%%%%%%%%::.  $$$$$$$$o.``???$$R?F.:%%%         \n')
delayPrint('      `$eu  %%%%%%% `$$$$$$$$$$$$er /%%%%%%%/          \n')
delayPrint('        `?$$eu. %%% t$$$$$$$$$$$$$! %%%%%%%%           \n')
print('\n')

# Logo
print(     '                      ,-, .--                            ')
print(     '                       /  `-.                            ')
print(     '                      \'-` `-\'                          ')
print(     '                                                         ')
print(     '                        /\                               ')
print(     '                       //\\\                             ')
print(     '                  |\   /  \   /|                         ')
print(     '                  |\\\ //  \\\ //|                       ')
print(     '                  ||\\\/    \//||                        ')
print(     '                  || //\  /\\\ ||                        ')
print(     '                  ||// \\\// \\\||                       ')
print(     '                  ||/_ _||_ _\||                         ')
print(     '                  └ ─ ─ ─ ─ ─ -┘                         ')
print(     '                                                         ')

# Line 4
delayPrint('                    歡 迎 光 臨                      \n\n', 'red')
# Line 5
delayPrint('              5525 回到那一天 BBS 站                 \n\n', 'cyan')
# Line 6
delayPrint('            Welcome to #5525 LIVE TOUR               \n', 'yellow')
# Bar line:
print()
print()
# Line 7
delayPrint('               Since  1997 . 3 . 29                   \n', 'green')
# Line 8
delayPrint('          本站開放 ')
delayPrint('5521~5525 ', 'yellow')
delayPrint('等五個port\n')
# Line 9
delayPrint('                   歡迎多加利用                       \n')
delayPrint('                  Coded by Laurie                       \n\n')

# City
print(Fore.CYAN + '                 _ _ _ _ _ _             _ _ _ _        ')
print(Fore.CYAN + ' _ _ _ _ _      |           |           |       |       ')
print(Fore.CYAN + '|         |     |           |           |┌ - - ┐ \      ')
print(Fore.CYAN + '| ┌ - - ┐ |     |           |_ _ _      ||     |  \     ')
print(Fore.CYAN + '| |     | |_ _ _|                 |     |└ - - ┘   \    ')
print(Fore.CYAN + '| └ - - ┘                         |     |           \   ')
print(Fore.CYAN + '|                                 |     |            \  ')
print(Fore.CYAN + '|                                 |_ _ _|             \ ')
print(Fore.CYAN + '|                                                      |')

# Dynamic bar
dynamicBar()







