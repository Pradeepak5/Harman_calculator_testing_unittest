def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def Mul(a,b):
    return a*b
def div(a,b):
    return a/b

if __name__=="__main__":
    a = int(input("Enter num1 :"))
    b = int(input("Enter num2 :"))

    addition = add(a, b)
    print(addition)
    subtraction = sub(a, b)
    print(subtraction)
    multiplication = Mul(a, b)
    print(multiplication)
    division = div(a, b)
    print(division)
