import datetime as d

S:str = "success"
W:str = "WARNING"
E:str = "ERROR"
N:str = "NONE"



fm_1:str = "%Y/%m/%d %H:%M:%S" #2023/01/01 01:00:00
fm_2:str = "%Y/%m/%a %H:%M:%S" #2023/01/Sun 01:00:00
fm_3:str = "%Y/%m/%d %H:%M"    #2023/01/01 01:00
fm_4:str = "%Y/%m/%a %H:%M"    #2023/01/Sun 01:00

fm_5:str = "%m/%d %H:%M:%S"    #01/01 01:00:00
fm_6:str = "%m/%a %H:%M:%S"    #01/Sun 01:00:00 
fm_7:str = "%m/%d %H:%M"       #01/01 01:00
fm_8:str = "%m/%a %H:%M"       #01/Sun 01:00

fm_9:str = "%H:%M:%S"          #01:00:00
fm_10:str = "%H:%M"            #01:00




class Palette:
    BLACK          = '\033[30m'
    RED            = '\033[31m'
    GREEN          = '\033[32m'
    YELLOW         = '\033[33m'
    BLUE           = '\033[34m'
    MAGENTA        = '\033[35m'
    CYAN           = '\033[36m'
    WHITE          = '\033[37m'
    COLOR_DEFAULT  = '\033[39m'
    BOLD           = '\033[1m'
    UNDERLINE      = '\033[4m'
    INVISIBLE      = '\033[08m'
    REVERCE        = '\033[07m'
    BG_BLACK       = '\033[40m'
    BG_RED         = '\033[41m'
    BG_GREEN       = '\033[42m'
    BG_YELLOW      = '\033[43m'
    BG_BLUE        = '\033[44m'
    BG_MAGENTA     = '\033[45m'
    BG_CYAN        = '\033[46m'
    BG_WHITE       = '\033[47m'
    BG_DEFAULT     = '\033[49m'
    RESET          = '\033[0m'



def check(mode):
    if S == mode:
        color = Palette.GREEN
        sign = "+"
    elif W == mode:
        color = Palette.YELLOW
        sign = "-"
    elif E == mode:
        color = Palette.RED
        sign = "!"
    else:
        color = Palette.RESET
        sign = " "
    return color, sign



def pr(text:str, mode = N, format:str=None) -> None:
    format = "%H:%M:%S" if not format else format
    color, sign = check(mode)
    print(f"{d.datetime.now().strftime(format)} - ({color}{sign}{Palette.RESET}) {color}{text}{Palette.RESET}")



def toFile(text:str, mode = N, format:str=None, file:str=None) -> None:
    format = "%H:%M:%S" if not format else format
    color, sign = check(mode)
    with open(file, "a") as f:
        f.write(f"{d.datetime.now().strftime(format)} - ({sign}) {text}\n")




