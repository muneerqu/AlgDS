#
#
#
import random


def main():
    x = random.randint(1, 1000)
    print(x)

    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

if __name__ == '__main__':
    main()
