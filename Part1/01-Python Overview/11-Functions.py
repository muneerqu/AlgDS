def function_x(x):
    print('Hello and the number is: {}'.format(x))
    return x+7


def function_y(x=99):
    print('Hello and the number is: {}'.format(x))


w = function_x(10)
function_y()

print('The value of w is: {}'.format(w))