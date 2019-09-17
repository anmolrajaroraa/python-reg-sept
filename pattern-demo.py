'''for i in range(10):
	print(' ' * (9-i),end='')
	print('*' * (2 * i + 1))'''

for i in range(10):
    for j in range(10):
        for k in range(10):
            if i == j and j == k and k == i:
                print(i,j,k)