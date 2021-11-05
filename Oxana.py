# 1
#--------

period = 2
n1 = int(input('Vvedite  pervoe celoe chislo:' ))
n2 = int(input('Vvedite  vtoroe celoe chislo:' ))
summa = n1 +n2 + period
print('summa cifr = ', n1+n2 + period)
 #2
 #---------->

sec = int(input('vvedite sec' ))
hour = sec // 3600
min  = (sec - ( hour * 3600)) // 60
# or
min = (sec // 3600) % 60
sec = (sec % 3600) % 60
print(hour, min, sec, sep=':')

# 3
#----------->
n = int(input('vvedite  celoe chislo n' ))
per = n * 11
vt = n * 111
sum = n + n * 1 + n * 111
print('summa = ', sum)

# 4
#------->

num = int(input('vvedite celoe pologhitelnoe chislo = '))
max_num = 0
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
        if max_num == 9:
            break
    num //=10

print(f'naibolshay cifra chisla: {max_num}')

#5
#------>
n = int(input('viruchka: '))
b = int(input('izderghki:'))
if b > n:
    print('ubitok')
elif n > b:
    print('pribil')
    rentabel = (n - b) / n
    print('Rentabel', rentabel)
    amount = int(input('Kolichestvo sotrudnikov: '))
    amount_one = (n - b) / amount
    print('Pribil na odnogo cotr:', amount_one)

# 6
#------->
a = float(input('Distance 1 day:'))
b = float(input('Target :  '))
days = 1
while a < b:
    a = a * 1.1
    days += 1
print('time; ', days)



