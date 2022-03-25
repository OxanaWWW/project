
def int_func(txt):
    word = txt[0].upper() + txt[1:].lower()
    return word


string = input('enter words with space:  ')
for word in string.split('  '):
    print(f'{int_func(word)}', end=' ')