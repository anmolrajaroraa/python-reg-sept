# a = 10
# b = 20
# c = 25
#
# def add():
#     #print(a + b)
#     #return None  #default statement
#     c = a + b
#     return c
#
# def sub(a,b):
#     return a - b if a > b else b - a
#
# def mul(a = 1,b = 1):    #default arguments
#     return a * b
#
# def div(a = 30, b = 0):
#     return a / b
#
# def calc(a,b):
#     result = [a+b , a-b, a*b, a/b]
#     return a+b, a-b, a*b, a/b, a%b, a**b    #packing
#     #return a-b
#
# #print(30)
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# '''result = sub(num1,num2)
# print(result)
#
# print(mul(num1))
#
# print(div(c,b = 50))  #mapping the arguments
# #print(
#
# #print(40)'''
#
#
# result = calc(num1,num2)
# print(result)
# add_result, sub_result, mul_result, div_result, *otherResults = calc(num1,num2)    unpacking
#
# #    *otherResults - > multiple args , *args  -> creates a list if used to store returned values
# # creates a tuple if used as a function argument
# #    **otherDetails - > keyword args , **kwargs  -> creates a dictionary
#
# print(add_result)
# print(sub_result)
# print(mul_result)
# print(div_result)
# print(otherResults)

#def student(id,name,course,address, *otherDetails):
def student(id,name,course,address, **otherDetails):
    print(f'''  Id = {id}
    course = {course}
    name = {name}
    address = {address}
    otherDetails = {otherDetails}''')

#student(101,'Ram', 'BTech', {'home': 'rohini', 'hostel': 'other city'}, '9810102020', '25')
student(101,'Ram', 'BTech', {'home': 'rohini', 'hostel': 'other city'})

