for _ in range(int(input())):
    first, second = [int(x) for x in input().split()]

    if second - first < 3:
        if first% 2 == 0 and second%2 == 0:
            print(first,second)
        else:
            print(-1)
    else:
        if first % 2 == 0:
            print(first,first+2)
        else:
            if first % 3 == 0:
                print(first,first+3)
            else:
                print(first+1,first+3)
