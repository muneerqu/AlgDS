#
#
#


class Parent:
    count = 0
    name = None
    age = None

    def __init__(self, name, age):
        print('This is Parent constructor')
        self.name = name
        self.age = age
        Parent.count += 1

    def display(self):
        print(f'Name: {self.name} Age: {self.age}')

    def pcout(self):
        print(f'Number of Parents {self.count}')


class Child(Parent):
    count = 0
    name = None
    age = None

    def __init__(self, name, age):
        print('This is Child constructor')
        self.name = name
        self.age = age
        Child.count += 1

    def display(self):
        print(f'Name: {self.name} Age: {self.age}')

    def ccout(self):
        print(f'Number of Parents {self.count}')


def main():
    print('This is main')
    p1 = Parent('pA', 30)
    p2 = Parent('pB', 35)
    c1 = Child('cA', 25)
    c1 = Child('cB', 34)
    p1.display()
    c1.display()
    p1.pcout()
    c1.ccout()


if __name__ == '__main__':
    main()



