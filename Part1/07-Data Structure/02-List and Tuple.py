#
#
#
def main():
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    # game.append('Computer')   # Gives error Tuple is not mutable


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()
