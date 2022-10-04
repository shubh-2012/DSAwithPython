
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a,b):
    return (a / gcd(a,b))* b

for _ in range(int(input())):
    size,A,B, target = [int(x) for x in input().split()]

    LCM = lcm(A,B)
    #count_A,count_B,count_lcm = 0,0,0
    #count = 0

    count_A = size // A
    count_B = size // B

    count_lcm = size // LCM

    count = count_B + count_A - 2 * count_lcm
    if count >= target:
        print("YES")
    else:
        print("NO")
