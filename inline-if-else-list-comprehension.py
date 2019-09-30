#Membership operators - in, not in
#Comparison operators -->    >=, <=, ==, !=, not, is
#Logical operators -> and, or

a = 10
b = 20
diff = (a - b) if (a > b) else (b - a)
#diff = a > b ? a - b : b - a

'''if a > b:
    diff = a-b
else:
    diff = b-a'''

print("Diff is", diff)

list1 = []

for i in range(0,101):
    if i % 2 == 0 and i % 3 == 0:
        list1.append(i)

#List Comprehension
#list = expression(code that needs to go inside loop)    for loop    if condition (optional)

list2 = [i for i in range(0,101) if (i % 2 == 0 or i % 3 == 0)]

list3 = [    i if (i % 2 == 0 or i % 3 == 0) else 'X'            for i in range(0,101)   ]

print(list3)

list4 = [  12, 23, 34, 56, 'hello', [11,22,33,44,55],    [66,77,88,99] , ['ram', 'shyam', 'mohan']]

element = input("Enter the element to check if it is present in list or not: ")

for char in element:
    if char.isalpha():
        break
else:
    element = int(element)


if element in list4:
    print("Element is present")
else:
    for i in list4:
        if type(i) == list:
            if element in i:
                print( "Element is present" )
                break
    else:
        print("Element not found")

'''if type(i) != list:
        if element == i:
            print("Element is present")
            break'''

'''        for j in i:
                if element == j:
                    print("Element is present")
                    break'''



'''for item in list4:
    if type(item) == int or type(item) == bool:
        print(item)
        continue
    for element in item:
        print(element)'''

'''for i in range(len(list4)):
    if type(list4[i]) == int or type(list4[i]) == bool:
        print(list4[i])
        continue
    for j in range(len(list4[i])):
        print(list4[i][j])'''