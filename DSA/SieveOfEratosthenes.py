#SieveOfEratosthenes(all prime numbers till n)

import math
def soe(n):
    prime = [True for i in range(0, n+1)]
    x = 2
    while(x*x <= n):
        if(prime[x] == True):
            for i in range(x*x, n+1, x):
                prime[i] = False
        x = x+1

    for i in range(2, n+1):
        if(prime[i] == True):
            print(i)

soe(50)