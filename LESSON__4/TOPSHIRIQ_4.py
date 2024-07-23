# plus , minus, divide , multiply
class Calculate:
    def __init__(self):
        pass

    def plus(self,son1,son2):
        if type(son1) == int or type(son1) == float and type(son2) == int or type(son2) == float :
            return son1+son2
        else: raise ValueError

    def minus(self,son1,son2):
        if type(son1) == int or type(son1) == float and type(son2) == int or type(son2) == float:
            return son1-son2
        else: raise ValueError

    def divide(self,son1,son2):
        if type(son1) == int or type(son1) == float and type(son2) == int or type(son2) == float:
            return son1 / son2
        else: raise ValueError

    def multiply(self, son1, son2):
        if type(son1) == int or type(son1) == float and type(son2) == int or type(son2) == float:
            return son1 * son2
        else:
            raise ValueError

mat = Calculate()
print(mat.plus(45, 5.3))
print(mat.minus(53.3, 89))
print(mat.divide(10,3.3))
print(mat.multiply(3,11))