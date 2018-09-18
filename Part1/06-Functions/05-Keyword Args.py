#
#
#

def main():
    kitten(Buffy='meow', Zilla='grr', Angel='rawr')
    print('###### using variable ########')
    x = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    kitten(**x)  # ** to pass dictionary


def kitten(**kwargs):  # ** like list arguments but as Dictionary instead of list {key1:'value1', key2:'value2'}
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow.')


if __name__ == '__main__': main()
