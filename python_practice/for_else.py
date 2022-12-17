# in for else is executed every time except when break is triggerred , even when the loop is not run at all
y = 0
for x in range(1,y):
    print(x)
    if x == 3:
        break
else:
    print('loop completed')

# for i in range(10,1,-2):  # for loop can be run backwards ,
#     print(i)


