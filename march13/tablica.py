print('''a=4 \nb=5''')
a = 4
b = 5
d = a*b
c = int(input('введите результат умножения первого числа на второе: '))
if c == d:
    print(f'ответ верный: {d}')
else:
    print(f'''Ответ: {c} \nНеверно. Правильный ответ {d}!''') 
