#
#
#
animal = ('bear', 'bunny', 'dog', 'cat', 'lion')

for i in animal:
    if i == 'dog': continue
    if i == 'cat': break
    print('The animal name is: {}'.format(i))