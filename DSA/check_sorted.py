
# check if given list is sorted or not

def check_sorted(list):
    for i in range(0,len(list)-1):
        if list[i]>list[i+1]:
            print("not sorted")
            return
    print("sorted")
    return

list = [1,2,4,3,4,5]
check_sorted(list)
