#
#
#
x = 20
y = 34
print('The numbers are {}, {}'.format(x, y))
print('The numbers are {1}, {0}, {0}, {1}'.format(x, y))
print('The numbers are {n1}, {n2}'.format(n1=x, n2=y))
print('The numbers are {n1:<5}, {n2:>5}'.format(n1=x, n2=y)) # formating/shifting left and right 0:< adding space
print('The numbers are {n1:<5}, {n2:>05}'.format(n1=x, n2=y)) # 1:<05 filling space with zeros




z = 200 * 14145
print('The number is {:,}'.format(z)) # addingg comma
print('The number is {:,}'.format(z).replace(',', '.')) # replace comma with dot
print('The number is {:f}'.format(z)) # define decimal points
print('The number is {:.3f}'.format(z)) # define decimal points
print('The number is {:x}'.format(z)) # define decimal points
print('The number is {:b}'.format(z)) # define decimal points
print(f'The number is {z:.3f}') # new format

