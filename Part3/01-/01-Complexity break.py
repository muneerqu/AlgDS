

def complexity(n):
    count = 0
    for i in range(int(n/2), n):
        j = 1
        count = count + 1
        while j + n / n <= n:
            break
            j = j * 2
            count = count + 1
    print(count)


def main():
    complexity(20)


if __name__ == '__main__':
    main()
