
import math
for _ in range(int(input())):
    shops, admins = [int(x) for x in input().split()]
    inputList = list(map(int, input().split()))

    x = min(inputList)

    if admins <= x :
        print(shops)
    else:
        print(math.ceil(admins / x))
