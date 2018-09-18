#
#
#
x = range(10)           # range in not mutable
for i in x:
    # x[5]=10           # gives Error
    print('Value of i is: {}'.format(i))

print('####################################')

for i in x:
    print('Value of i is: {}'.format(i + 1))

print('####################################')

x = range(5, 50)
for i in x:
    print('Value of i is: {}'.format(i))

print('####################################')

x = range(5, 50, 5)
for i in x:
    print('Value of i is: {}'.format(i))

print('####################################')

x = list(range(10))     # list is mutable 
x[5]=555
for i in x:
    print('Value of i is: {}'.format(i))
