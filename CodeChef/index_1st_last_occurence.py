#find index of first and last occurence of element in sorterd array

def find_occurence(list,x):
    first=-1
    last=-1
    for i in range(0,len(list)):
        if list[i] == x:
            last = i
        if list[i] == x and first == -1 :
            first = i
    print(first,last)

list=[1,2,3,4,4,4,5]
find_occurence(list,4)
