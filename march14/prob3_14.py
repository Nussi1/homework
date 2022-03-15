names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
even = []
for i in range(0, len(names[0:11])):
	if i % 2:
		even.append(names[i])

print(even + names[10:])
