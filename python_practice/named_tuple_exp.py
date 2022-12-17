from collections import namedtuple

HistData = namedtuple('HistData','open high low close')
print(type(HistData))

h1 = HistData(10,15,3,7)

tup_list = []
tup_list2 = []
for x in range(5):
    h2 = HistData(x,x+1,x-2,x-5)
    tup_list.append(h2)
    tmp_row = [x,x+1,x-2,x-5]
    tup_list2.append(tmp_row)

print(tup_list.__sizeof__())
print(tup_list)
print(tup_list2.__sizeof__())
print(tup_list2)
for y in tup_list:
    print(y.open,y.high,y.low,y.close)

