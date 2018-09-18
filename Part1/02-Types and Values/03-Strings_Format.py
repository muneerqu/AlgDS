#
#
#
x = 10
z = 22

a = 'nine'.capitalize()
print('x is: {}'.format(a))
print(type(a))

a = 'nine is a number'.capitalize().title()
print('x is: {}'.format(a))
print(type(a))

a = 'nine {} {}'.format(8, 9)
print('x is: {}'.format(a))
print(type(a))


a = 'nine {1} {0}'.format(8, 9)
print('x is: {}'.format(a))
print(type(a))

a = 'nine {1:<9} {0:>9}'.format(8, 9)
print('x is: {}'.format(a))
print(type(a))

a = 'nine "{1:<9}" "{0:>9}"'.format(8, 9)
print('x is: {}'.format(a))
print(type(a))

a = 'nine "{1:<09}" "{0:>09}"'.format(8, 9)
print('x is: {}'.format(a))
print(type(a))

a = 'nine "{1:<09}" "{0:>09}"'.format(8, 25456)
print('x is: {}'.format(a))
print(type(a))

a = 'nine {} {}'
print('x is: {}'.format(a))
print(type(a))

a = f'nine {x} {z}'
print('x is: {}'.format(a))
print(type(a))