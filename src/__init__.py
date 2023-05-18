__copyright__ = "Copyright (C) 2023 PySimpleLog"
__version__   = "2.0.0"
__author__    = "Ennui#9999"
__discord__   = "https://discord.gg/immaculate"


import datetime


__all__ = [
    'TimeFormat', 'PySimpleLog', "Color"
    ]



class TimeFormat:
    """Userfull Timeformat for strftime"""
    DEFAULT = "%Y/%m/%d (%a) %H:%M:%S" #2023/01/01 (Sun) 01:00:00
    ONE     = "%Y/%m/%d (%a) %H:%M"    #2023/01/01 (Sun) 01:00
    TWO     = "%Y/%m/%d %H:%M:%S"      #2023/01/01 01:00:00
    THREE   = "%Y/%m/%d %H:%M"         #2023/01/01 01:00

    FOUR    = "%m/%d (%a) %H:%M:%S"    #01/01 (Sun) 01:00:00
    FIVE    = "%m/%d (%a) %H:%M"       #01/01 (Sun) 01:00 
    SIX     = "%m/%d %H:%M:%S"         #01/01 01:00:00
    SEVEN   = "%m/%d %H:%M"            #01/01 01:00

    EIGHT   = "%H:%M:%S"               #01:00:00
    NINE    = "%H:%M"                  #01:00
    TEN     = "%M:%S"                  #00:00



class Color:
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
    
    """Aliases"""
    B  = BLACK
    R  = RED
    G  = GREEN
    Y  = YELLOW
    BR = BLUE
    M  = MAGENTA
    C  = CYAN
    W  = WHITE
    RS = RESET 



class PySimpleLog:
    def __init__(
        self, default:str="", symbol:str=" ", color=Color.M, time_format:str=TimeFormat.DEFAULT 
    ) -> None:

        self.S:str = "SUCCESS"
        self.W:str = "WARNING"
        self.E:str = "ERROR"
        self.N:str = "NONE"
        self.defualt = default
        self.symbol  = symbol
        self.color   = color if color is not None else ""
        self.time_format = time_format
    
    
    def check(self, mode) -> str:
        if self.S == mode:
            color = Color.G
            symbol = "+"

        elif self.W == mode:
            color = Color.Y
            symbol = "-"

        elif self.E == mode:
            color = Color.R
            symbol = "!"
            
        else:
            color = Color.RS
            symbol = " "
            
        return color, symbol


    def println(self, args, mode=None) -> None:
        COLOR, SYMBOL = self.check(mode if mode is not None else self.S)
        print(f"{datetime.datetime.now().strftime(self.time_format)} ({COLOR}{SYMBOL}{Color.RS}) {self.color}{args}{Color.RS}")