import platform


def main():
    message()


def message():
    print('The version of this python is {}'.format(platform.python_version()))
    print('Exiting version statement ...')


if __name__ == '__main__': main()
