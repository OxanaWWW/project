# 1

some_typs = [2, 2.3, [3,3,3,3], complex(), False, None, b'text',  'oxana', {1 :'x', 3 :'z'}, 'me']

for a in some_typs:
    print(type(a))

#2

input_list = list(input('list: '))
len_list = len(input_list)
i = 0
if len_list > 1:
    while i < len_list - 1:
        input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
        i += 2

print(input_list)



#3

x_month = input('enter num of month: ')
w,sp, su,  au = 'winter', 'spring', 'summer', 'autumn'
month_dict = {'1': w, '2': w,'3': sp, '4': sp, '5': sp, '6': su, '7': su, '8' : su, '9': au, '10': au, '11' : au, '12': w}
print(month_dict[x_month])

year = [w,w,sp,sp,sp,su,su,su,au,au,au,w]
print(year[int(x_month) - 1])

#4
abraca = input('sentence:  ')
words = abraca.split()
for n, word in enumerate(words):
    print((n + 1), (word[:10]))


#5
my_list = [8,8,8,7,6,5,5,4,3,2,1]
new_num = int(input('enter new_num:  '))
xx = False
for z, y in enumerate(my_list):
    if new_num > y:
        my_list.insert(z,new_num)
        xx = True
        break
if not xx:
    my_list.append(new_num)

print(my_list)

# 6

my_prodact = []
full_charact = {'name': [], 'price': [], 'amount': [], 'unit': []}
num = 1
command = input('want to add product?')

while  command != 'no':
        name = input('name:   ')
        price = input('price:  ')
        amount = input('amount:   ')
        unit = input('unit:   ')
        my_prodact.append((num, {'name': name, 'price': price, 'amount': amount, 'unit': unit}))
        num += 1
        command = input('want to stop product?')
        if command == 'stop':
            break

analit_list = {}
for num, full_charact in my_prodact:
    for key  ,value in full_charact.items():
        if not analit_list.get(key):
            analit_list[key] = [value]
        else:
            analit_list[key].append(value)

for key, value in analit_list.items():
    analit_list[key] = list(set(value))
print(analit_list)

