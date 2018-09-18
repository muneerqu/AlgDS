#
#
#
def main():
    kitten(5)
    dog(1, 5, 4)
    lion(4, 8)


def kitten(x):
    print('kitten!')
    print(x)


def dog(x, y, z):
    print('dog!')
    print(x, y, z)


def lion(x, y, z=10):
    print('lion!')
    print(x, y, x)


if __name__ == '__main__': main()
