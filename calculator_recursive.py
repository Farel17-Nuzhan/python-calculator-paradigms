class InvalidOperationError(Exception):
    pass
try:
    while(True):
        ans= []
        num_1= int(input("Enter first variable: "))
        num_2= int(input("Enter second variable: "))
        operation= input("Enter Operation to be performed: ")
        match operation:
            case "addition" | "+":
                print(f"{num_1 + num_2} is the answer of {operation} on {num_1} and {num_2}.")
                ans.append(num_1 + num_2)
            case "subtraction" | "-":
                print(f"{num_1 - num_2} is the answer of {operation} on {num_1} and {num_2}.")
                ans.append(num_1 - num_2)
            case "multiplication" | "*":
                ans.append(num_1 * num_2)
                print(f"{num_1 * num_2} is the answer of {operation} on {num_1} and {num_2}.")
            case "division" | "/":
                if (num_2 != 0):
                    ans.append(num_1 / num_2)
                    print(f"{num_1 - num_2} is the answer of {operation} on {num_1} and {num_2}.")
                else:
                    raise ZeroDivisionError
            case _:
                raise InvalidOperationError  
        x= input("Do you wish to continue?(Y/N): ")
        if x.lower() == "n":
            break

except ZeroDivisionError:
    print("The Operation is invalid.")
except InvalidOperationError:
    print("The Operation is beyond our capabilities.")
except ValueError:
    print("Invalid Input.")