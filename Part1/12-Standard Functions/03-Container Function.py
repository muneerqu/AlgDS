#
#
#
x = (1, 2, 3, 4, 5)
y = len(x)
y = reversed(x)
y = list(reversed(x))
y = sum(x)
y = sum(x, 10)
y = min(x)
y = max(x)
y = any(x)
y = all(x)  # return true if all greater and 0

w = (1, 2, 3, 4, 5)
v = (6, 7, 8, 9, 10)

z = zip(w, v)

print(x)
print(y)
for a, b in z:
    print(f'{a} and {b}')
