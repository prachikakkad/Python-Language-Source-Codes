class Operator_Overloading:

    def __init__(self , num1):
        self.num1 = num1

    def __add__(self, num2):
        print("Lets Add")
        return self.num1 + num2.num1

    def __sub__(self, num2):
        print("Lets Subtract")
        return self.num1 - num2.num1

    def __mul__(self , num2):
        print("Lets Multiply")
        return self.num1 * num2.num1

    def __truediv__(self , num2):
        print("Lets Divide")
        return self.num1 / num2.num1

    def __floordiv__(self , num2):
        print("Lets Floor Divide")
        return self.num1 // num2.num1

num_1 = Operator_Overloading(28)
num_2 = Operator_Overloading(6)
print(Operator_Overloading.__add__(num_1 , num_2))
print(Operator_Overloading.__sub__(num_1 , num_2))
print(Operator_Overloading.__mul__(num_1 , num_2))
print(Operator_Overloading.__truediv__(num_1 , num_2))
print(Operator_Overloading.__floordiv__(num_1 , num_2))