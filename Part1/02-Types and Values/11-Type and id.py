#
#
#
x = (1, 'two', 3, [4, 'four'], 5)  # each element is object
y = (1, 'two', 3, [4, 'four'], 5)  # x and y are classes of type tuple

print('The value of x is: {}'.format(x))
print(type(x))
print(id(x))

print('The value of x is: {}'.format(y))
print(type(y))
print(id(y))

print('''
############
''')
print(id(x[1]))
print(id(y[1]))

if x[1] is y[1]:  # is x[1] same object as y[1]
    print('They are the same value')
else:
    print('They are different values')

if isinstance(x, tuple):
    print('tuple')
elif isinstance(x, list):
    print('list')
elif isinstance(x, set):
    print('set')
elif isinstance(x, dict):
    print('dict')
else:
    print('different type')

print('''
############
''')

y = [1, 'two', 3, [4, 'four'], 5]
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
elif isinstance(y, set):
    print('set')
elif isinstance(y, dict):
    print('dict')
else:
    print('different type')