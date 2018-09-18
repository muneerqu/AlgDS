#
#
#
def main():
    x = kitten()
    print(f'{x} | {type(x)}')
    y = dog()
    print(f'{y} | {type(y)}')
    z = lion()
    print(f'{z} | {type(z)}')
    c = cat()
    print(f'{c} | {type(c)}')


def kitten():
    print('Meow.')


def dog():
    return 20


def lion():
    return 'rawwwwr'


def cat():
    return {1, 2, 3, 4, }


if __name__ == '__main__': main()
