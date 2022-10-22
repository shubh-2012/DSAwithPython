#squares of even numbers between 0 to 99


def square(x):
    return (x*x)

def iseven(x):
    return (x%2 == 0)

a = list(map(square,filter(iseven,range(100))))

print(a)