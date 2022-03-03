p = int(input('enter profit:   '))
l = int(input('enter loss: '))
if p > l:
    print(f' profitability : {p // l}')
    k = int(input('enter numbers employees:   '))
    print(f'profit per person: {p // k}')
else:
    print(f'deficit: {l}')