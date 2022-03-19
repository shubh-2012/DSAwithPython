for _ in range(int(input())):
    size = [int(x) for x in input().split()]
    inputList = list(map(int, input().split()))
    count_even, count_odd, odd_count = 0, 0, 0
    for i in range(0, len(inputList)):
        if inputList[i] % 2 == 0:
            count_even = 1
        else:
            count_odd += 1
            odd_count = 1

    if count_odd % 2 == 0:
        if count_even == 1:
            odd_count = 0
        print(count_even + odd_count)
    else:
        if count_even == 1:
            print(odd_count + count_even)
        else:
            if count_odd > 1:
                print(2)
            else:
                print(1)