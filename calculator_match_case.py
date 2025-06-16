num_1: int = int(input("Enter first number: "))
num_2: int = int(input("Enter second number: "))

operation: str = input("Enter the operation to be performed: ")

match operation:
    case "add" | "addition" | "+":
        print(f"The answer is {num_1 + num_2} after performing {operation} on {num_1} and {num_2}.")
    case "sub" | "subtraction" | "-":
        print(f"The answer is {num_1 - num_2} after performing {operation} on {num_1} and {num_2}.")
    case "product" | "multiplication" | "*":
        print(f"The answer is {num_1 * num_2} after performing {operation} on {num_1} and {num_2}.")
    case "quotient" | "division" | "/":
        if num_2 == 0:
            print("Invalid Operation.")
        else:
            print(f"The answer is {num_1 / num_2} after performing {operation} on {num_1} and {num_2}.")
    case _:
        print(f"{operation} is beyond my capabilities.")
