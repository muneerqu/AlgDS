#
#
#
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in x:
    print('The value of i is: {}'.format(i))

print('###################################')
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x[1] = 11
x[4] = 44
x[8] = 88
for i in x:
    print('The value of i is: {}'.format(i))
