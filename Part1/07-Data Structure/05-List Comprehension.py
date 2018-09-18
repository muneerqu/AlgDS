#
#
# List Comprehension is a list based on another list or iterator


def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    print_list(seq)
    print('###################')
    print_list(seq2)
    print('###################')
    seq2 = [x for x in seq if x % 3 != 0]  # list of list not divied by zero
    print_list(seq2)
    print('###################')
    seq2 = [(x, x ** 2) for x in seq]  # list of list not divied by zero
    print_list(seq2)
    print('###################')
    from math import pi
    seq2 = [round(pi, i) for i in seq]  # list of list not divied by zero
    print_list(seq2)
    print('###################')
    seq2 = {x: x ** 2 for x in seq}  # list of list not divied by zero
    print(seq2)
    print('###################')
    seq2 = {x for x in 'superduper' if x not in 'pd'}  # list of list not divied by zero
    print(seq2)


def print_list(o):
    for x in o: print(x, end=' ')
    print()


if __name__ == '__main__': main()
