#
#
#

class Animal:
    x = [1, 2, 3]   # this list is associated with the class and mutable in main
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t=None):
        if t: self._type = t
        return self._type

    def name(self, n=None):
        if n: self._name = n
        return self._name

    def sound(self, s=None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print(a0)
    print(a1)
    a0._name = 'joe'  # _ variables shouldn't be accessed like private in C++
    print(a0.name())
    print(a0.x)
    a1.x[0] = 9         # change the value for all objects related to class Animal
    print(a0.x)



if __name__ == '__main__': main()
