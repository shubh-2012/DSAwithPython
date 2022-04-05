for _ in range(int(input())):
    n = int(input())
    initial = n
    num = n
    n = n+1
    sum,sum1 = 0,0
    while(num != 0 ):
        sum += num % 10
        num //= 10
    while(n != 0):
        sum1 += n % 10
        n //= 10
    if sum % 2 == 0 and sum1 % 2 != 0:
        print(initial+1)
    elif sum % 2 != 0 and sum1 % 2 == 0:
        print(initial+1)
    else:
        print(initial+2)









