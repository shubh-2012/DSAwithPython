
def insertionSort(inputList):
    for slicedEnd in range(len(inputList)):       #increase the size of the sorted array
        pos = slicedEnd
        while pos > 0  and inputList[pos] < inputList[pos -1]:    #move from right to left
            (inputList[pos],inputList[pos-1]) = (inputList[pos-1],inputList[pos]) #swap
            pos = pos - 1




for _ in range(int(input())):
    size = [int(x) for x in input().split()]
    inputList = list(map(int, input().split()))

    insertionSort(inputList)
    print(inputList)

