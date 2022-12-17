"""
create a list of named tuples and use inbuilt sorted function to generate a new list sorted on 'key' volume in
descending order

"""

from collections import namedtuple
import datetime

his_data = namedtuple("Hdata",'strike expiry volume')

# a = his_data(strike=17500,expiry='123',volume=500)

tup_list = [
    his_data(strike=17500,expiry='123',volume=500 * x) for x in range(10)
]


# for a in tup_list:
# print(a.strike,a.expiry,a.volume)

new_list = sorted(tup_list,key= lambda trade: trade.volume,reverse=True)

print(tup_list)
print(new_list)

dic_list = [
    {'name':'a','month':'Apr21','fy':2021},
    {'name':'a','month':'Dec22','fy':2022},
    {'name':'a','month':'Jan22','fy':2021},
    {'name':'a','month':'Jul22','fy':2022},
]
func = lambda y:datetime.datetime.strptime(y['month'],"%b%y")

# dic_list.sort(key=lambda x:(x['fy'],func),reverse=True)
dic_list.sort(key=lambda x:(x['fy'],datetime.datetime.strptime(x['month'],"%b%y")),reverse=True)

for i in dic_list:
    print(i)
print('-'*20)
dic_list.sort(key=lambda x:(-x['fy'],datetime.datetime.strptime(x['month'],"%b%y")))

for i in dic_list:
    print(i)
