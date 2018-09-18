#
#
#

def main():
    # animals = dict(kitten='meow', puppy='ruff!')
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
               'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    for k, v in animals.items():
        print(f'{k} do {v}')
    print('###################')
    for k in animals.keys(): print(k)
    print('###################')
    for v in animals.values(): print(v)
    print('###################')
    print(animals['lion'])
    print('###################')
    animals['lion'] = 'GRRRRRR'
    print(animals['lion'])
    print('###################')
    animals['monkey'] = 'hahahahahah'
    print(animals['monkey'])
    print('###################')
    print('lion' in animals)
    print('###################')
    print_dict(animals)


def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')


if __name__ == '__main__': main()
