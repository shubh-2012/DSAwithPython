

def hello(n):
    if(n == 0):
        return
    hello(n-1)
    print("hello", n)

hello(10)
