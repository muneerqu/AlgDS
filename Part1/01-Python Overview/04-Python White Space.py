import platform


def main():
    message()


def message():
    print('The version of this python is {}'.format(platform.python_version()))
    print('Exiting version statement ...')
    if True:
        print('This is True: another level')
    else:
        print('This is False: another level')


print('Before the main function')

if __name__ == '__main__': main()
