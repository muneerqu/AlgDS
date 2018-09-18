#
#
#
import sys, os


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    v = sys.platform
    print(v)

    v = os.path
    print(v)
    v = os.name
    print(v)
    v = os.getcwd()
    print(v)
    v = os.urandom(25).hex()
    print(v)



if __name__ == '__main__':
    main()
