
def sum_dig(n):
    if(n==0):
        return 0.
    return sum_dig(n//10) + n % 10

print("sum of digits of is: ",sum_dig(234))