"""
WAP a program in python ot implement a calculator that operator using concepts of
OOP
Decorators: A function that takes another function as an argument and returns a new function.
Setters and Getters
Static and Class Method
Magic Dunder
Exception Handling
Map, Filter and Reduce
Walrus Operators
args and Kwargs
File Handling
OS and Shutil Modules
Command Line Utilities
"""

import time

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Initiating the operation...")
        result = func(*args, **kwargs)
        return result
    print("Initiating the session...")
    return wrapper



class InvalidOperationError(Exception):
    """Raised when an invalid operation is specified."""
    pass

@decorator
def calculator(x: int ,y: int ,a: str )-> int | None :
    """
    Performs a mathematical operation on two integers based on the specified operator.

    Args:
        x (int): The first number.
        y (int): The second number.
        a (str): The operation to perform. Must be one of 'addition', 'subtraction', 
                'multiplication', 'division', or their symbols ('+', '-', '*', '/').

    Returns:
        int | None: The result of the operation, or None if an error occurs.

    Raises:
        ZeroDivisionError: If division is attempted with y = 0.
        InvalidOperationError: If an invalid operation is specified.
    """
    try: 
        # Map operation strings to mathematical operations
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

    except ZeroDivisionError:
        print(f"The denominator cannot be 0 for division operation.")
    except InvalidOperationError:
        print("The operation is not possible with my current capabilities.")
    except Exception as e:
        print(f"The program did not execute because {e}.")


if __name__ == "__main__":
    start_measure_time = time.time()
    results: list[int | str] = []
    # Continuously prompt user for inputs until they choose to exit
    while True:
        try:
                x: int = int(input("Enter first number: "))
                y: int = int(input("Enter second number: "))
                a: str = input("Enter what operation to perform(addition, subtraction, division, multiplication): ")

                # print(f"The value of {x} and {y} upon performing {a} is {"Invalid Attempt" if(t:=calci(x, y, a)) is None else t}.")
                print(f"Performing {a} on {x} and {y} is an {(t:= 'Invalid Attempt' if (t := calculator(x, y, a)) is None else t)}.")
                results.append(t)

        except Exception as e:
            print(f"The execution did not work because {e}.")

        s: str = input("do you want to continue (Y/N): ")

        if s.upper() != "Y":
            print(f"All results from operations: {results}.")
            print("Terminating the session...")
            print("Thank you for choosing us.")
            end_measure_time = time.time()
            print(f"The time taken by the program is: {end_measure_time - start_measure_time:.4f} seconds.")
            break

if __name__ != "__main__":
    calculate= decorator(calculator)
