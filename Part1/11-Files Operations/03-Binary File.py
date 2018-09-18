#
#
#
def main():
    infile = open('pic.jpg', 'rb')
    outfile = open('pic-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\ndone.')


if __name__ == '__main__': main()
