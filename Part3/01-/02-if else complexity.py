
def if_condition(n):            # O(1)
    x = n
    if x == 0:
        x = x + 1
    print(x)


def if_else_condition(n):
    x = n
    if x == 0:
        x = x + 1
    else:
        x += 2
    print(x)


def if_else_condition_2(n):
    x = n
    if x > 0:
        for x in range(1, n):
            print(x)
    else:
        x += 2
    print(x)


def if_else_condition_3(n):          # O(n^2)
    x = n
    if print_function(n):
        for j in range(x):
            print(j)
    elif x < 0:
        x += 2
    print(x)


def print_function(n):
    for i in range(n):
        print(i)


def main():
    n = 20
    # if_condition(n)             # O(1)
    # if_else_condition(n)        # O(1)
    # if_else_condition_2(n)      # O(n)
    if_else_condition_3(n)      # O(^2)
    # print_function(n)


if __name__ == '__main__':
    main()
