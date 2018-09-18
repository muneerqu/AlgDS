#
#
#
def main():
    infile = open('file.txt', 'rt')
    outfile = open('file-copy.txt', 'wt')
    for line in infile:
        # print(line.rstrip(), file=outfile)
        outfile.write(line)
        print('.', end='', flush=True)
    outfile.close()
    infile.close()
    print('\ndone')


if __name__ == '__main__':
    main()
