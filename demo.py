#this is a comment
'''print('hello python. ', sep='')
print('python is a programming lang')'''

'''
This is a multi-line comment.
Python isn't going to execute this.
'''

first_num = int(input("Enter first number: "))
second_num = 5
#total = first_num + second_num
#diff = int(first_num) - second_num
prod = first_num * second_num
q = first_num / second_num #classic divide (ans is in float)
q2 = first_num // second_num #floor divide (ans is in integer)

#print("Sum of " + str(first_num) + " and " + str(second_num) + " is " + str(total))
#print("Sum of",first_num,"and",second_num,"is",total)

#print("Diff b/w %s and %d is %d"%(first_num, second_num, diff))

print("Product of {} and {} is {}".format(first_num, second_num, str(prod)))

print(f"{first_num} / {second_num} = {q}")
