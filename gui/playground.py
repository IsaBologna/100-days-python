def add(*args):
    sum = 0
    for n in args:
        sum = n + sum
    return sum

def calculate(**kwargs):
    print(kwargs)
    print(kwargs["add"])

calculate(add=3, multiply=5)

s = add(1,2,3,4,5,6,7,8,9)
