#
#
#


class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: The number of this object is {self._n}'

    def __str__(self):
        return f'str: The number of this object is {self._n}'


b = Bunny(23)
e = Bunny('🐰')
print(repr(b))
print(b)
print(ascii(b)) # This skip any character no ascii
print(repr(e))
print(ascii(e))
print(ord('🐰'))
print(chr(128048))
# s = 'Hello World!'
# print(repr(s))
