for _ in range(int(input())):
    size = int(input())
    inputList = list(map(int, input().split()))

    inputList.sort()
    pairCount = 0
    nonPairCount = 0
    totalCount = 0
    i = 0
    while i < len(inputList) - 1:
        if inputList[i] == inputList[i + 1]:
            pairCount += 1
            i += 2
        else:
            nonPairCount += 1
            i += 1

    if pairCount*2 + nonPairCount < size:
        nonPairCount += 1

    oddpairCount = pairCount % 2
    if oddpairCount == 1:
        if nonPairCount>=1:
            totalCount += 1
            nonPairCount -= 1
        else:
            totalCount += 2

    totalCount += (nonPairCount // 2) * 2
    if nonPairCount % 2 != 0:
        totalCount += 3


    print(totalCount)





