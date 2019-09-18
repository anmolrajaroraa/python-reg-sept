'''number = int(input("Enter the number to check if it's prime or not: "))

flag = True
if number<=1:
    print(number, "is not a prime number")
else:
    for i in range(2, number // 2):
        if number % i == 0:
            print(number, "is not a prime number")
            flag = False
            break
    if flag:
        print(number, "is a prime number")'''

number = int(input("Enter the number to check if it's prime or not: "))

if number<=1:
    print(number, "is not a prime number")
else:
    for i in range(2, number // 2):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

