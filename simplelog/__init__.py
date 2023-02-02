from .src import *


__copyright__ = "Copyright (C) 2023 Palette"
__version__   = "1.0.0"
__author__    = "Ennui#9999"
__discord__   = "https://discord.gg/Ennui"


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







def pr(text:str, mode = N, format:str=None) -> None: ...


def toFile(text:str, mode = N, format:str=None, file:str=None) -> None: ...