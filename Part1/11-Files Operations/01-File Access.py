#
#
#
def main():
    f = open('file.txt')    # default read mode only 'r', 'w' write mode after emptying file
    # for line in f:        'a' append,'r+' read and write 'r+b' binary mode, 'r+t' text mode
    # for line in f:        '
    for line in f:
        print(line.rstrip()) # strip line without the carriage return and white space at the end of line
        # print(line)


if __name__ == '__main__':
    main()
