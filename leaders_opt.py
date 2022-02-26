def leaders1(list):
    n= len(list)
    result = []
    max_n = list[n-1]
    result.append(list[n-1])
    for i in range(n-2,-1,-1):
        if list[i] >= max_n:
            result.append(list[i])
            max_n = list[i]

    result = result[::-1]
    print(result)

list = [1,6,2]
leaders1(list)


