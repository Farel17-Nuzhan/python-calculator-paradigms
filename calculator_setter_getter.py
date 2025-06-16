class InvalidOperatorError(Exception):
    pass

class Calculator:
    Operator= None
    _answer= []
    def __init__(self, num_1, num_2):
        self.x= num_1
        self.y= num_2

    @classmethod
    def operator(cls, operator):
        cls.Operator= operator
    
    def calculation(self):
        match Calculator.Operator:
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
    @property
    def answer(self):
        return(self.__class__._answer)
    @answer.setter
    def answer(self, ans):
        type(self)._answer.append(ans)

try:
    while(True):
        num_1= int(input("Enter first variable: "))
        num_2= int(input("Enter second variable: "))
        # operation= input("Enter Operation to be performed: ")
        
        ram= Calculator(num_1,num_2)
        ram.operator(input("Enter Operation to be performed: "))
        m= ram.calculation()
        print(m)
        ram.answer=m
        print(type(ram))
        x= input("Do you wish to continue?(Y/N): ")
        if x.lower() == "n":
            print(f"All the answers up till now are: {ram.answer}")
            break
    
except ZeroDivisionError:
    print("The given task is invalid.")

except InvalidOperatorError:
    print("The given task is beyond my capabilities.")

except ValueError:
    print("Invalid Input.")