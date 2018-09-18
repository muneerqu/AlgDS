#
#
#
import sys


def main():
    try:
        # x = int('foo')
        x = 5 / 3
    except ValueError:
        print('Fount a ValueError')
    except ZeroDivisionError:
        print('Divided by Zero Error')
    else:
        print('No Errors')

    try:
        x = 5 / 0

    except:
        print(f'Found an Error: {sys.exc_info()}')


print('Hello World!')

if __name__ == '__main__':
    main()
