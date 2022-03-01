#binary search

def binary_search(list,start,end,x):
    if end >= start:
        mid = start + (end-start)//2

        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return binary_search(list,start,mid-1,x)

        else:
            return binary_search(list,mid+1,end,x)
    else:
        return -1

list = [1,2,3,5,8,9]
x= 4

result = binary_search(list,0,len(list)-1,x)

print(result)
