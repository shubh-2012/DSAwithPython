#find max difference between any two elements of list

def max_diff(list):
    min_n = list[0]
    max_n = list[0]
    for i in range(1,len(list)):
        if list[i]<min_n:
            min_n = list[i]
        elif list[i]>max_n:
            max_n = list[i]
    print(max_n-min_n)

list=[2,1,5,3]
max_diff(list)