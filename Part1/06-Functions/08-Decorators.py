#
#
#
# def f1():
#     print('Thi is f1')
#
#
# x = f1
# x()
# print('##############')


def g1():
    def g2():
        print('This is g2')
    return g2

# g2()   # Error can not be reached
x = g1()
x()
