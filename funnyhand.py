for _ in range(int(input())):
    size, A,B = [int(x) for x in input().split()]
    count = 0
    if abs(A-B) == 1:
        if A != 1 and B != 1 and A != size and B != size:
            count = 2
        else:
            count = 1
    if abs(A-B) == 2:
        count = 1
    print(count)
