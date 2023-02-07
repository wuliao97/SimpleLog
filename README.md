# SimpleLog
## Currently in production


## usage
```py
from simplelog import *

pr("test message", S)

pr("error message", E)


pr("Warning message", W, "%d:%M")

pr("None", format=fm_2)
```

### Output
![image](https://github.com/wuliao97/SimpleLog/blob/main/images/Screenshot%202023-02-02%20165630.png)

## Option
```py
#mode of pr color

S:str = "success" #'\033[32m'
W:str = "WARNING" #'\033[33m'
E:str = "ERROR"   #'\033[31m'
N:str = "NONE"    #'\033[0m'



#mode of datetime format

import enum

class TimeFormat(enum.Enum):
    DEFAULT = "%Y/%m/%d (%a) %H:%M:%S" #2023/01/01 (Sun) 01:00:00
    ONE     = "%Y/%m/%d (%a) %H:%M"    #2023/01/01 (Sun) 01:00
    TWO     = "%Y/%m/%d %H:%M:%S"      #2023/01/01 01:00:00
    THREE   = "%Y/%m/%d %H:%M"         #2023/01/01 01:00

    FOUR    = "%m/%d (%a) %H:%M:%S"    #01/01 (Sun) 01:00:00
    FIVE    = "%m/%d (%a) %H:%M"       #01/01 (Sun) 01:00 
    SIX     = "%m/%d %H:%M"            #01/01 01:00
    SEVEN   = "%m/%d %H:%M"            #01/01 01:00

    EIGHT   = "%H:%M:%S"               #01:00:00
    NINE    = "%H:%M"                  #01:00

    def __str__(self):
        return str(self.value)
```

Thank you.
