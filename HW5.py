def nozero(fnc):
    def helper(*args):
        print("inside the service")
        print(fnc(*args))
        print("outside the service")
    return helper
@nozero
def div(x, y):
    print("div function called")
    return x / y

@nozero
def mul(x, y):
    print("mul function called")
    return x * y

@nozero
def add(x, y):
    print("add function called")
    return x + y
@nozero
def sub(x, y):
    print("sub function called")
    return x - y
div(10,5)
mul(25,25)
add(60,50)
sub(100,20)

