x = 15
y = 36
z = 9

if x < y:
    print('x is smaller than y')
else:
    print('y is smaller than x')

if z < x: print('one line: z is smaller than y')

if y < x:
    print('y is greater than x')
elif z < y:
    print('z is smaller than y')
else:
    print('do something')

# like switch in C++
if x == 16:
    print('The value of x is: {}'.format(x))
elif y == 33:
    print('The value of y is: {}'.format(y))
elif z == 9:
    print('The value of z is: {}'.format(z))
