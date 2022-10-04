#count digits in a number

def count_dig(n):
    count = 0
    while(n>0):
        count+=1
        n = n//10
    return count
print("number of digits is",count_dig(123))
