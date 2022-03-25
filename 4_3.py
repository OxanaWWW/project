def my_func(x,y):
    if x < 0:
        return 'x must be greater than 0'
    if y > 0:
        return ' y must be less than 0'
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z


x = float(input('enter positive number - x:  '))
y = int(input('enter negative number - y:  '))
print(my_func(x,y))