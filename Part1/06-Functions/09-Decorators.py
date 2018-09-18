#
#
#

def g1(g):
    def g2():
        print('This is g2 before function call')
        g()
        print('This is g2 after function call')
    return g2

@g1                     # called decorator
def g3():               # called function definition
    print('This is g3')


# x = g1(g3)
# x()

g3()  # use this instead of the above assignment lines