for _ in range(int(input())):
    size = int(input())
    i = 0
    if size == 1:
        print(3)
    else:
        n = pow(10,size - 1) + i
        while n % 3 != 0 or n % 9 == 0 or n%2 == 0:
            n += 1

        print(n)

