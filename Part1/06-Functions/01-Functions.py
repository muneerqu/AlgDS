#
#
#
def main():
    k = kitten(100, 50, 10)
    print('main: Function name is: {}'.format(__name__))  # shows the name of the module if imported
    print(f'The value of kitten is: {k}')
    p = purr(50)
    print(f'The value of purr is {p}')


def kitten(x, y, z):
    print(f'{x}: Meow.')
    print(f'{y}: Meow.')
    print(f'{z}: Meow.')
    print('kitten: Function name is: {}'.format(__name__))  # shows the name of the module if imported


def purr(x):
    print(f'{x+1}: purrrr {x} +1')
    return x + 1


if __name__ == '__main__': main()
