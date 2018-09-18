#
#
#
def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1:3])
    print(game[0:4:2])
    i = game.index('Paper')
    print(game[i])
    game.append('Computer')
    game.insert(0, 'Radio')
    print_list(game)
    game.remove('Lizard')
    n = game.pop()          # remove from the end of the list
    print(n)
    m = game.pop(2)         # remove by index
    print(m)
    print_list(game)
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    del game[1:3]           # remove by slice
    print_list(game)
    print(', '.join(game))  # join each item with ,
    print(len(game))

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()
