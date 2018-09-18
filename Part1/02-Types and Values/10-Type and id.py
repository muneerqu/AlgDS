#
#
#
x = 9
print('The value of x is: {}'.format(x))
print(type(x))

print('''#######
#######''')

x = (1, 2, 3, 4, 5)
print('The value of x is: {}'.format(x))
print(type(x))

print('''#######
#######''')

x = (1, 'two', 3, [4, 'four'], 5)
print('The value of x is: {}'.format(x))
print(type(x))

print('''#######
#######''')

for i in x:
    print(type(i))
