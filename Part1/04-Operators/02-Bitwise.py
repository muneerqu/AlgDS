#
# Operate on bits
# & and | or ^ Xor << shift left >> shift right

x = 0x0a # a in hex is 10
y = 0x02 # 2 in hex is 2
z = x & y

# 02x is 2 char: string 0 means hex 2 char wide x hex display of int value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')

# 02x is 8 char: string 0 means hex 8 char wide b binary display of int value
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

print('#########################')

x = 0x0a # a in hex is 10
y = 0x02 # 2 in hex is 2
z = x | y

# 02x is 2 char: string 0 means hex 2 char wide x hex display of int value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')

# 02x is 8 char: string 0 means hex 8 char wide b binary display of int value
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

print('#########################')

x = 0x0a # a in hex is 10
y = 0x05 # 2 in hex is 2
z = x | y

# 02x is 2 char: string 0 means hex 2 char wide x hex display of int value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')

# 02x is 8 char: string 0 means hex 8 char wide b binary display of int value
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')


print('#########################')

x = 0x0a # a in hex is 10
y = 0x05 # 2 in hex is 2
z = x ^ y

# 02x is 2 char: string 0 means hex 2 char wide x hex display of int value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')

# 02x is 8 char: string 0 means hex 8 char wide b binary display of int value
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')


print('#########################')

x = 0x0a # a in hex is 10
y = 0x05 # 2 in hex is 2
z = x << y

# 02x is 2 char: string 0 means hex 2 char wide x hex display of int value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')

# 02x is 8 char: string 0 means hex 8 char wide b binary display of int value
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')


print('#########################')

x = 0x0a # a in hex is 10
y = 0x05 # 2 in hex is 2
z = x >> y

# 02x is 2 char: string 0 means hex 2 char wide x hex display of int value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')

# 02x is 8 char: string 0 means hex 8 char wide b binary display of int value
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')