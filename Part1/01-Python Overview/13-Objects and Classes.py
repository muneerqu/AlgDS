#
#
#
#
class Duck:
    sound = 'Quack!'
    walking = 'Walks like a duck'
    def quack(self):
        # print('Quack!')
        print(self.sound)

    def walk(self):
        # print('Walks like a duck.')
        print(self.walking)


def main():
    Donald = Duck()
    Donald.quack()
    Donald.walk()


if __name__ == '__main__': main()
