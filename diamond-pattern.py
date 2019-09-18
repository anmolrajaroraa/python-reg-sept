'''








'''
for i in range(20):
	counter = i
	if i==10:
		continue
	if i<10:
		for j in range(10 - counter):
			print(' ', end='')
		for k in range(2 * counter - 1):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print(' ', end='')
		for k in range(((19 - counter) * 2) - 1):
			print('*', end='')
	print()