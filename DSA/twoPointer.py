# find pair that add to target in a sorted array

def findpair(list, x):
    i = 0
    j = len(list) - 1

    while i < j:
        if list[i] + list[j] == x:
            return (list[i], list[j])
        elif list[i] + list[j] < x:
            i += 1
        elif list[i] + list[j] > x:
            j -= 1
        else:
            print("no pair found")
            return -1



list=[1,2,3,4,5]

ans = findpair(list,15)
print(ans)