def calc(x,y,opr):
    print(eval(x + opr + y))

while True:
    print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit''')

    choice = input("Enter your choice: ")

    operations = {"1" : '+', "2" : '-', "3" : '*', "4" : '/'}

    operation = operations.get(choice)

    num1 = input( "Enter first number: " )
    num2 = input( "Enter second number: " )

    calc(num1,num2,operation)