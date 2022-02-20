
def pattern(n):
    if(n==1):
        print("*\n")
        return
    for i in range(1,n+1):
        print("*",end="")
    print('\n')
    pattern(n-1)
    for i in range(1,n+1):
        print("*",end="")
    print('\n')


pattern(5)