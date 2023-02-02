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
