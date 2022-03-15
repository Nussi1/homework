city = ['New-Delhi', 'Neu-Ulm', 'Barselona']
city.append('Bishkek')
print(city)
city [2] = 'Munich'
print(city)
city.remove('New-Delhi')
print(city)
york = input('Введите название города: ')
print(york)
new = []
for i in city:
	if york != city:
		new.append(york)
	elif york in city:
		print(f'Такой город уже есть! {york} ') 
print(i)
