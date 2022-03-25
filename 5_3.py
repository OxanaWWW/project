def sum_num(num_str, stop):
    num_list = num_str.split(' ')
    sum_list = 0
    for i in num_list:
        if i == stop:
            break
        sum_list += int(i)


    return  sum_list


stopper = '#'
finished = False
s = 0
while not finished:

    num_str_user = input('enter number with space:  ')
    s += sum_num(num_str_user, stopper)
    finished = stopper in num_str_user
    print(f'Sum = {s}')
