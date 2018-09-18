#
#
# and And or Or not Not in Value in not in Value not in is Some object identity in not Not same object


a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if a and b:
    print('expression 1 is true')
else:
    print('expression 1 is false')

if not a:
    print('expression 2 is true')
else:
    print('expression 2 is false')

if y in x:
    print('expression 3 is true')
else:
    print('expression 3 is false')

if y not in x:
    print('expression 4 is true')
else:
    print('expression 4 is false')

if y is x[0]:
    print('expression 4 is true')
else:
    print('expression 4 is false')
