#
#
# Generator is a special class of function that act as an iterator instead of return a single value
# it returns a stream of values

def main():
    # for i in range(25):

    for i in inclusive_range(5,25,5):
        print(i, end=' ')
    print()


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__': main()
