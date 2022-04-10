for _ in range(int(input())):
    n = int(input())

    if (n-2)% 4 == 0 or (n-2) % 4 == 1:
        print(3)
    elif (n-2)% 4 == 2:
        print(n+3)
    elif (n-2)% 4 == 3:
        print(n)