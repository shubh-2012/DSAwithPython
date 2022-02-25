list = [1,2,3,4,5]
def swap(list):
    n = len(list)
    a = list[0]
    list[0] = list[n-1]
    list[n-1] = a

swap(list)
print(list)
