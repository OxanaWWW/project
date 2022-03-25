def user_info(name, surname, age, city, mail, phone):
    print(f'{name} {surname}{age}{city}{mail}{phone}')

    ''' enter real name'''


n = input('name:  ')
s = input('surname:  ')
a = input('age:  ')
c = input('city:  ')
m = input('mail:  ')
p = input('phone:  ')
user_info(name=n, surname=s, age=a, city=c, mail=m, phone=p)
