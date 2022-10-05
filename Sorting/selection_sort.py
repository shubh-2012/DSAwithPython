
def sel_sort(inputList):
    for i in range(len(inputList)):
        minimum = i
        for j in range(i, len(inputList)):
            if inputList[j] < inputList[minimum]:
                minimum = j

        (inputList[i], inputList[minimum]) = (inputList[minimum], inputList[i])


for _ in range(int(input())):
    size = [int(x) for x in input().split()]
    inputList = list(map(int, input().split()))

    sel_sort(inputList)
    print(inputList)

