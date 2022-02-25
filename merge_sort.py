# MergeSort


def mergeSort(list):
    if len(list) > 1:

        mid = len(list) // 2
        L = list[:mid]
        M = list[mid:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            list[k] = M[j]
            j += 1
            k += 1

def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print()


if __name__ == '__main__':
    list = [6, 5, 12, 10, 9, 1,6]

    mergeSort(list)

    print("Sorted array is: ")
    printList(list)