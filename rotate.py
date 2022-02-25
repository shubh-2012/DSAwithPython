def rotate(list,n,d):
    if(d>n):
        d = d%n
    list[:] = list[d:n] + list[0:d]
    return list
n = int(input("enter size of list: "))
d = int(input("enter number of elements to rotate: "))

list=[]
for i in range(0,n):
    a = int(input())
    list.append(a)

result = rotate(list,n,d)

print(result)



