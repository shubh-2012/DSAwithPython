
def insertionSort(inputList):
    for slicedEnd in range(len(inputList)):
        pos = slicedEnd
        while pos > 0  and inputList[pos] < inputList[pos -1]:
            (inputList[pos],inputList[pos-1]) = (inputList[pos-1],inputList[pos])
            pos = pos - 1




for _ in range(int(input())):
    size = [int(x) for x in input().split()]
    inputList = list(map(int, input().split()))

    insertionSort(inputList)
    print(inputList)

