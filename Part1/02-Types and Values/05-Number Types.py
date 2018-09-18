#
#
#
from decimal import *

x = .1 + .1 + .1 - .3
print('x value is: {}'.format(x))
print(type(x))

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x value is: {}'.format(x))
print(type(x))
