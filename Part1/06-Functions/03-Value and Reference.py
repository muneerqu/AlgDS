#
#
#   Assigning mutable means Assigning a reference to the mutable and can be changed as a pointer/references
def main():
    # print(__name__)
    x = 5
    y = x
    print(id(x))
    print(id(y))
    print('#######################')
    x = 5
    y = x
    y = 3
    print(id(x))
    print(id(y))
    print('#######################')
    x = [5]
    y = x
    y[0] = 3
    print(id(x))
    print(id(y))
    print('#######################')
    print(x[0])
    print('#######################')
    print(f'x before kitten() is: {x[0]}')
    kitten(x)
    print(f'x after kitten() is: {x[0]}')


def kitten(n):          # works like pointer/references in C++
    n[0] = 10


if __name__ == '__main__': main()
