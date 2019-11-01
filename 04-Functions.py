'''list1 = ['ram','shyam','mohan','mike','jim']

for i in range(len(list1)):
    print(f"{i+1}. {list1[i]}")

for index,name in enumerate(list1, start = 1):
    print(f"{index}. {name}")'''


# def temp_convert(c):
#     return 9/5 * c + 32
#
# temp = [0,11,22,33,44,55,66,77,88,99]
#
# # print(temp_convert(temp))
#
# f_temp = []
#
# for t in temp:
#     f_temp.append(temp_convert(t))
#
# print(f_temp)
#
# f_temp = [temp_convert(t) for t in temp]
#
# print(f_temp)
#
# f_temp = list(map(temp_convert, temp))
#
# print(f_temp)
#
# f_temp = list(map(lambda c : 9/5 * c + 32, temp))
#
# print(f_temp)
#
# f_temp = [  (lambda c : 9/5 * c + 32)(t) for t in temp]



def even(n):
    return n % 2 == 0

numbers = list(range(1,101))
#newList = list(map(even, numbers))
newList = []
'''for n in numbers:
    if even(n):
        newList.append(n)'''
newList = [n for n in numbers if even(n)]
newList = [n for n in numbers if (lambda n : n%2== 0)(n)]
#newList = list(filter(even, numbers))
#newList = list(filter(lambda n: n % 2 == 0,numbers))
print(newList)

def someFn(element):   #[101, 'Ram']
    return element[1]   #'Ram'

list1 = [[101, 'Ram'], [103, 'Shyam'], [102, 'Mohan'], [104, 'Raman']]
# list1.sort(key = someFn)  #'Ram'
list1.sort(key = lambda element : element[1])
print(list1)