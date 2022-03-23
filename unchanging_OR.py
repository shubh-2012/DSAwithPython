
import math
for _ in range(int(input())):
    target = int(input())

    power = math.floor(math.log(target,2))
    i = power
    count = 0
    while(i>0):
        count += pow(2,i)//2 -1
        i -= 1

    extra = target - (pow(2,power))

    print(count + extra)


