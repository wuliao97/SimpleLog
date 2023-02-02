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
```
16:49:39 - (+) test message
16:49:39 - (!) error message   
02:49 - (-) Warning message    
2023/02/Thu 16:49:39 - ( ) None
```

## Option
```py
#mode of pr color

S:str = "success" #'\033[32m'
W:str = "WARNING" #'\033[33m'
E:str = "ERROR"   #'\033[31m'
N:str = "NONE"    #'\033[0m'


#mode of datetime format

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
```

Thank you.
