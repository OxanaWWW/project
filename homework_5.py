#1***********************8
with open('test.txt', 'w') as file:
    input_line = input('Text :\n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line = input('Text :\n')


#2*********************

with open('test.txt') as file:
    file_lines = file.readlines()
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        words_count = len(line.split())
        print(f'#{num + 1} - {words_count} words')
    print(f'{str_count} strings')

#3*******************************

with open('../test_3.txt') as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
average_sal = sum_salary / len(employees)
print(f' Average = {average_sal}')


for k, v in employees.items():
    if v < 20000:
        print(f'{k}: {v}')

#4************************
nums = {
    'one': 'odin',
    'two': 'dwa',
    'three': 'tri',
    'four': 'chetire',
}


with open('test_4.txt') as file, open('new_file.txt', 'w') as new_file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        rus_nume = nums.get(data[0])
        new_file.write(f'{line.replace(data[0], rus_nume)}')

#5*************
#
import random

with open('test_num.txt', 'w') as file:
    for _ in range(30):
        file.write(f'{random.randint(0,10)} ')

with open('test_num.txt') as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)

print(sum)

##6*********************

results = {}
with open('test_5.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        # check all numbers
        hours = 0
        for elem in data[1:]:
            if elem != '-':
                num = '0'
                # write number
                for i in elem:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int(num)

        results.update({data[0].strip(':'): hours})
print(results)

#7********************

import json

companies = {}
pos_count, pos_sum = 0, 0
with  open('test3.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        companies.update(({data[0]: profit}))
        if profit > 0:
            pos_count += 1
            pos_sum += profit

average_profit = pos_sum / pos_count
result = [companies, {'average_profit': average_profit}]

with open('result.json', 'w') as file:
    json.dump(result, file)