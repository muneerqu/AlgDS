#
#
#
s = 'This is a string to test how to split and join Python Strings'

print(s)
print(s.split()) # split based on white space
my_list = s.split()
print(my_list)

print(s.split('i')) # split based char i

s2= ':'.join(my_list)
print(s2)