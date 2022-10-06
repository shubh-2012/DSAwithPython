
def mergeSort(self,nums1:list[int],m: int, nums2:list[int],n:int) -> None:

    i = j = k = 0

    while i < nums2 and j < n:
        if nums1[i] < nums2[j]:
            list[k] = nums1[i]
            i += 1
        else:
            list[k] = nums2[j]
            j += 1
        k += 1

    while i < len(nums1):
        list[k] = nums1[i]
        i += 1
        k += 1

    while j < len(nums2):
        list[k] = nums2[j]
        j += 1
        k += 1

def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print()


