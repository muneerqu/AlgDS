#
#
#

class MyString(str):
    def __str__(self):
        return self[::-1]


a = 'Hello World! This is Python'
print('Hello World! This is Python'.lower())
print('Hello World! This is Python'.title())
print('Hello World! This is Python'.capitalize())
print('Hello World! This is Python'.swapcase())

print(a.lower())
print(a.upper())
print(a.capitalize())

print('Class MyString')

s = MyString('Hello World!')
print(s)

print('''
Hello 
World {}'''
      .format(10 * 9))
print()
print('Hello World! This is Python'.casefold())
