class InvalidOperationError(Exception):
     pass

def decorator(func):
    def wrapper(*args,**kwargs):
        print("Initializing Decorator...")
        answer: int =func(*args,**kwargs)
        print("Operation Successful...")
        return answer
    return wrapper

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
    operation= input("Enter the operation to be performed: ")

    dec= decorator(calculator)
    print(f"The answer is {dec(num_1,num_2,operation)} after performing {operation} in {num_1} and {num_2}.")


except ZeroDivisionError:
    print("The given task is invalid.")

except InvalidOperationError:
    print("The given task is beyond my capabilities.")

except ValueError:
    print("Invalid Input.")