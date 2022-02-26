def leaders(list):
    n= len(list)
    result = []
    a = 0
    for i in range(0,n-1):
        for j in range(1,n):
            if list[i]>list[j]:
                a+=1
            else:
                a = 0
                continue
        if(a == (n-1-i)):
            result.append(list[i])
            a = 0
    result.append(list[n-1])
    print(result)

list = [1,2,4,3,2,1]
leaders(list)


