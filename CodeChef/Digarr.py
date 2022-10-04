for _ in range(int(input())):
    size = int(input())
    n = int(input())
    x = 0
    mod = 10
    while(size!=0):
        if n % mod == 5 or n% mod == 0:
            x = 1
            break
        else:
            size -= 1
            n = n//10

    if x == 1:
        print("YES")

    else: print("No")

