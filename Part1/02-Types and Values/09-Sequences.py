#
#
# Dictionary


x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x:
    print('i value is: {}'.format(i))  # This print only the value

print('######################################')

for k, v in x.items():
    print('key "{0}" value is: {1}'.format(k, v))  # This print the value and the key

print('######################################')

x['four'] = 44              # Dictionary is mutable
for k, v in x.items():
    print('key "{0}" value is: {1}'.format(k, v))  # This print the value and the key
