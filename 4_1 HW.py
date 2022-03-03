n = int(input('enter number:   '))
max_n = 0
while n > 0:

    if n == 9:
        break
    if n % 10 > max_n:

         max_n = n % 10
    n //= 10
print(f'max number: {max_n}')