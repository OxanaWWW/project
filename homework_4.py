#***************1********
import sys

if len(sys.argv) < 4:
    print(f'enter all data(production, norma, premium')
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    result = a * b + c
    print(result)

#***2**********
num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num_list[i] for i in range(1, len(num_list)) if num_list[i] > num_list[i - 1]]
print(result)

#3****************************

result = [x for x in range(20,241) if ((x % 20 == 0) or (x % 21 == 0))]
print(result)

#4*************************

num_list = [2, 2, 2, 7, 23, 1, 44,  44, 3, 2, 10, 7, 4, 11]
result = [x for x in num_list if num_list.count(x) == 1]
print(result)


#5******************

from functools import  reduce

num_list = [x for x in range(100, 1001,2)]
print(reduce(lambda a,b: a* b, num_list))

#6***********************

from itertools import cycle,count

n = 100
num_list = [x for x in range(5)]
counter = count()
cycler = cycle(num_list)
print([next(counter) for x in range(n)])
print([next(cycler) for x in range(n)])

#7***********************

def gen_factorial(number):
    c = 1
    for i in range(1, number +1):
        c *= i
        yield c


n = 11
for ind, el in enumerate(gen_factorial(n)):
    print(f'#{ind + 1} {el}')