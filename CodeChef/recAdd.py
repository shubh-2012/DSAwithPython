def fun1(x, y):
    if (x == 0):
        return y
    else:
        return fun1(x - 1, x + y)

print(fun1(3,6))

def fun2(n):
    if(n == 1):
        return 0
    else:
        return 1 + fun2(n//2)

print(fun2(8))