#
#
#
#


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


def list_prime(n):
    for x in range(n):
        if isprime(x):
            print(x, end=' ', flush=True)
    print()


n = 7
list_prime(100)
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')
