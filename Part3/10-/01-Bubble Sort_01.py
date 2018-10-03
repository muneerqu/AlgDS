
def bubblesort(A):
    for i in range(len(A)):
        for k in range(len(A)-1, i, -1):
            if (A[k] < A[k-1]):
                swap(A, k, k-1)


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


def main():
    mylist = [452, 677, 123, 452, 694, 42, 544, 134, 587, 900]
    bubblesort(mylist)
    print(mylist)


if __name__ == '__main__':
    main()
