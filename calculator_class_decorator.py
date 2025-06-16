class InvalidOperationError(Exception):
     pass

class decorator:
    def __init__(self,func):
        self.func= func
        print("Decorator is ready for action...")
    def __call__(self,*args,**kwargs):
        print("Initializing decorator...")
        x= self.func(*args,**kwargs)
        print("Operation successful...")
        return x


@decorator
def calculator(x,y,a):
    match a:
                case "addition" | "+":
                    return x+y
                case "subtraction" | "-" :
                    return x-y
                case "multiplication" | "*":
                    return x*y
                case "division" | "/":
                    if y==0:
                        raise ZeroDivisionError()
                    return x/y
                case _:
                    raise InvalidOperationError

try:                
    num_1= int(input("Enter first number: "))
    num_2= int(input("Enter second number: "))
    operation= input("Enter operation (addition, subtraction, multiplication, division): ")
    print(f"The answer is {calculator(num_1,num_2,operation)} after performing {operation} on {num_1} and {num_2}.")

except ZeroDivisionError:
    print("The given task is invalid.")

except InvalidOperationError:
    print("The given task is beyond my capabilities.")

except ValueError:
    print("Invalid Input.")