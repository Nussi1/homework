a = 17391 % 17
b = 546 % 17
c = 934 % 17
if a < b and a < c:
	print('a < b,c')
elif b < a and b < c:
	print('b < a,c')
else: 
	print('c < a,b')
