#check prime
import math

val = int(input('enter number to check: '))
a = math.floor(math.sqrt(val))+1
n = 0
for i in range(1,val+1):
    if(val%i) == 0:
        n=n+1

print(n)





    #if val % i == 0:
        #print('Not a Prime Number, divisible by ')
        #print(i)
        #break
    #elif i == math.floor(math.sqrt(val)) : print('Prime Number')






