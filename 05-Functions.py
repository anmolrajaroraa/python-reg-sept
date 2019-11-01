'''def outer():
    print("Outer called")
    def inner1():
        return "inner1 fn"
    def inner2():
        return "inner2 fn"

    #print(inner1())
    #print(inner2())
    #print("Last statement")
    return inner1,inner2

inner_fns = outer()
print(inner_fns[0]())
print(outer()[1]())'''




x = 10    #global variable
y = 20
def add():
    global x
    x = x + 1
    print(x + y)

add()
print("X is ", x)

'''def outer():
    x = 10
    print("X in outer is",x)
    def inner():
        global x
        x = 100
        print("X in inner is",x)
    inner()
    print("X in outer is",x)

outer()
print("X globally is",x)'''