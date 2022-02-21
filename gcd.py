
#def gcd(a,b):
    #if(a == 0):
       # return b
    #if(b==0):
        #return a
    #if(a>b):
        #return gcd(a-b,b)
    #return gcd(a,b-a)

#print(gcd(98,56))

def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)

print(gcd(10,15))

def lcm(a,b):
    return (a*b)//gcd(a,b)

print(lcm(10,15))
