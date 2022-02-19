
#fibonnaci

num = int(input('enter a num : '))

def fib(n):
    a=0
    b=1

    if n == 0:
        return a
    elif n== 1:
        return b
    else:
        return fib(n-1) + fib(n-2)

print('fib for given inpt is: ',fib(num))