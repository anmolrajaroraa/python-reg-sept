#try - put all the logic here
#except (type of error that needs to be handled) - write code that is going to handle the error

def divide():
    num1 = int( input( "Enter first number: " ) )
    num2 = int( input( "Enter second number: " ) )

    print( num1 / num2 )

try:
    divide()
except TypeError:
    print("Some error occured..")
except ZeroDivisionError:
    print("Cannot divide by zero")
    divide()
except ValueError:
    print("Please enter only integers")
    divide()
except BaseException as error:
    print("Please try some time later..", error)