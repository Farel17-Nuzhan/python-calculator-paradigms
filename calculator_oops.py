class InvalidOperatorError(Exception):
    pass

class Calculator:
    Operator= None
    def __init__(self, num_1, num_2):
        self.x= num_1
        self.y= num_2

    @classmethod
    def operator(cls, operator):
        cls.Operator= operator
    
    def calculation(self, Op):
        match Op:
            case "addition" | "+":
                return self.x + self.y
            case "subtraction" | "-" :
                return self.x - self.y
            case "multiplication" | "*":
                return self.x * self.y
            case "division" | "/":
                if self.y==0:
                    raise ZeroDivisionError()
                return self.x / self.y
            case _:
                raise InvalidOperatorError


    @staticmethod 
    def add(x,y):
        return(x + y)
    @staticmethod 
    def sub(x,y):
        return(x - y)
    @staticmethod 
    def quotient(x,y):
        if y==0:
            raise ZeroDivisionError
        return(x / y)
    @staticmethod 
    def product(x,y):
        return(x * y)
    @staticmethod
    def nothing():
        raise InvalidOperatorError

try:
    ram= Calculator(23,32)
    print(Calculator.Operator)
    ram.operator("division")
    print(Calculator.Operator)
    print(ram.calculation("addition"))
    
except ZeroDivisionError:
    print("The given task is invalid.")

except InvalidOperatorError:
    print("The given task is beyond my capabilities.")

except ValueError:
    print("Invalid Input.")