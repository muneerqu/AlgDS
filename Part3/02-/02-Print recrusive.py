def Print(n):
    if n == 0: 
        return 0
    else:
        print(n)
        return Print(n-1)

def main():
    Print(100)


if __name__ == '__main__':
    main()
