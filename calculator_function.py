class InvalidOperatorError(Exception):
    pass

def Calculator(a: int , b: int ,c: str) -> int:
    """
    A Calculator that can perform addition, subtraction, multiplication and division provided

    Args:
        a (int): The first number.
        b (int): The second number.
        c (str): Operation to be performed.
    
    Returns:
        int: The answer after performing the calculation
    """
    if c == "addition" or c == "add" or c == "+":
        return(a+b)
    elif c == "subtract" or c == "sub" or c == "-":
        return(a+b)
    elif c == "Multiplication" or c == "Product" or c == "*":
        return(a+b)
    elif c == "Division" or c == "Quotient" or c == "/":
        if b == 0:
            raise ZeroDivisionError
        return(a+b)
    else:
        raise InvalidOperatorError
    
print("---------Calculator---------")
try:
    operation: str = input("Enter the operation you want to perform: ")
    num_1: int = int(input("Enter first number: "))
    num_2: int = int(input("Enter second number: "))

    # Calling a function that takes the given number as input and performs the operation specified by the user and return the value
    answer: int = Calculator(num_1, num_2, operation)

    print(f"The answer is {answer} after performing {operation} on {num_1} and {num_2}.")

except ZeroDivisionError:
    print("The given task is invalid.")

except InvalidOperatorError:
    print("The given task is beyond my capabilities.")

except ValueError:
    print("Invalid Input.")