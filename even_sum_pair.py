for _ in range(int(input())):
    A, B = [int(x) for x in input().split()]

    countOdd_A = 0
    countOdd_B = 0
    countEven_A = 0
    countEven_B = 0
    ans = 0
    countEven_A = A//2
    countOdd_A = A - countEven_A

    countEven_B = B // 2
    countOdd_B = B - countEven_B

    ans = countOdd_B*countOdd_B + countEven_A*countEven_B

    print(ans)