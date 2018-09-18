#
#
#

def main():
    kitten('meow', 'grrr', 'purr', 'add 1', 'add 3', 'add 4')
    x = ('meow', 'grrr', 'purr', 'add 1', 'add 3', 'add 4')
    kitten(*x)  # passing list as a reference


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')


if __name__ == '__main__': main()
