
def del_num(a, b):
    if b == 0:
        return "dont divide by 0"
    else:
        return a / b

a = float(input('a:  '))
b = float(input('b: '))
print(del_num(a, b))

#variant 2************
def del_num(a, b):
    try:
        a, b = int(a), int(b)
        del_num =a / b
    except ValueError:
        return  'ValueError'
    except ZeroDivisionError:
        return 'Division "0" forbidden'
    return round(del_num, 2)
print(del_num(input('enter a:  '), input('enter b:  ')))

