import random

def expo(zxc, number, p):
    res = 1
    zxc = zxc % p

    while number > 0:

        if number % 2:
            res = (res * zxc) % p
            number = number - 1
        else:
            zxc = (zxc ** 2) % p
            number = number // 2

    return res % p


def checkPrime(number, k):
    if number == 1 or number == 4:
        return False
    elif number == 2 or number == 3:
        return True

    else:
        for i in range(k):
            zxc = random.randint(2, number - 2)
            if expo(zxc, number - 1, number) != 1:
                return False
    return True

for _ in range(int(input())):
    first, second = [int(x) for x in input().split()]
    if first == 1 or second == 1:
        print(-1)
    elif first % 2 == 0  and second % 2 == 0:
        print(0)
    elif first % 3 == 0  and second % 3 == 0:
        print(0)
    elif checkPrime(first,3) and second % first == 0:
        print(0)
    elif checkPrime(second,3) and first % second == 0:
        print(0)
    else:
        print(1)

