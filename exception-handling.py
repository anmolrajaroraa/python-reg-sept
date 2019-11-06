#try - put all the logic here
#except (type of error that needs to be handled) - write code that is going to handle the error
#else - will run if there is no error in try, will not if some exception is there

#user defined exceptions -> raise, assert

# def divide():
#     num1 = int( input( "Enter first number: " ) )
#     num2 = int( input( "Enter second number: " ) )
#
#     print( num1 / num2 )
#
# try:
#     divide()
# except TypeError:
#     print("Some error occured..")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
#     divide()
# except ValueError:
#     print("Please enter only integers")
#     divide()
# except BaseException as error:
#     print("Please try some time later..", error)

balance = 10000
def withdraw():
    global balance
    pin = 1234
    pinInput = int(input("Please enter PIN: "))
    '''if pinInput != pin:
        print("Incorrect PIN")
        raise ValueError("Pin was not correct")'''

    assert(pin == pinInput), "Pin incorrect"

    amount = int(input("Enter the amount you want to withdraw: "))
    '''if amount > balance:
        print("Insufficient balance")
        raise ValueError("Balance is not enough")'''

    assert amount<= balance, "Insufficient balance"
    balance -= amount
    print("Updated balance is", balance)
def checkBalance():
    print("Current balance is", balance)


try:
    withdraw()
    checkBalance()
except AssertionError as err:
    print(err)
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except BaseException as err:
    print(err)
else:
    print( "Thank you for visiting!" )
