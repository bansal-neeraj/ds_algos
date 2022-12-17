
from enum import Enum


class Delta(Enum):
    D10 = 0.10
    D25 = 0.25
    ATM = 0.5


print(Delta.D10.value)
print(Delta.D25.value)
print(Delta.ATM.value)



class TimeBin(Enum):
    SHORT_DATE = (0,7)
    WEEKLY = range(6,12)

# print(TimeBin.SHORT_DATE.value[0],TimeBin.SHORT_DATE.value[1])

class CheckRange:
    def __init__(self):
        self.weekly = range(TimeBin.SHORT_DATE.value[0],TimeBin.SHORT_DATE.value[1])

obj1 = CheckRange()


print(TimeBin.WEEKLY.value)
if 15 in obj1.weekly:
    print("weekly data")
else:
    print("NOT")

print(list(TimeBin.WEEKLY.value))

if 50 in TimeBin.WEEKLY.value:
    print('weekly option')
else:
    print('other option')
