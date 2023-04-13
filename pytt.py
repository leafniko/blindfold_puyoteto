import random
import ctypes

mode = input("1:color(str),2:number,3:tt(str),4:color,5:tt:")
mode = int(mode)

if mode==4 or mode==5:
    ENABLE_PROCESSED_OUTPUT = 0x0001
    ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING
   
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    kernel32.SetConsoleMode(handle, MODE)

    END = '\033[0m'
    RED = f'\033[31m■{END}'
    BLUE = f'\033[34m■{END}'
    GREEN = f'\033[32m■{END}'
    YELLOW = f'\033[33m■{END}'
    PURPLE = f'\033[35m■{END}'
    BLACK = f'\033[30m■{END}'
    CYAN = f'\033[36m■{END}'
    WHITE = f'\033[37m■{END}'
   
    L = f"""{YELLOW}{BLACK}
{YELLOW}{BLACK}
{YELLOW}{YELLOW}"""
    Z = f"""{RED}{RED}{BLACK}
{BLACK}{RED}{RED}"""
    S = f"""{BLACK}{GREEN}{GREEN}
{GREEN}{GREEN}{BLACK}"""
    J = f"""{BLACK}{BLUE}
{BLACK}{BLUE}
{BLUE}{BLUE}"""
    I = f"""{CYAN}
{CYAN}
{CYAN}
{CYAN}"""
    O = f"""{YELLOW}{YELLOW}
{YELLOW}{YELLOW}"""
    T = f"""{PURPLE}{PURPLE}{PURPLE}
{BLACK}{PURPLE}{BLACK}"""


if mode == 1:
    set_list = ["赤","青","緑","黄","紫"]
elif mode == 3:
    set_list = ["L","Z","S","J","I","O","T"]
elif mode == 5:
    set_list = [L,Z,S,J,I,O,T]
elif mode == 4:
    set_list = [RED,BLUE,GREEN,YELLOW,PURPLE]
else:
    set_list = list(range(1,6))

if mode == 3 or mode == 5:
    tt_cycle = list(range(len(set_list)))
else:
    rm_py = random.choice(set_list)
    tmp_set = [i for i in set_list if i != rm_py]

while True:
    if mode == 3 or mode == 5:
        tmp_num = tt_cycle[random.randint(0,(len(tt_cycle)-1))]
        tt_cycle = [i for i in tt_cycle if i != tmp_num]
        result = set_list[tmp_num]
        if len(tt_cycle)==0:
            tt_cycle = list(range(len(set_list)))
    else:
        result = str(tmp_set[random.randint(0,3)]) + str(tmp_set[random.randint(0,3)])
    print(result)
    waiting = input("")
    if waiting == "end":
        break