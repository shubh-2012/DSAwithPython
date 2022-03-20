for _ in range(int(input())):
    size = int(input())
    inputList = list(map(int, input().split()))

    even_list = []
    odd_list = []

    for i in range(0, len(inputList)):
        if inputList[i] % 2 == 0:
            even_list.append(inputList[i])
        else:
            odd_list.append(inputList[i])

    if len(odd_list) <= 1:
        print(-1)
    elif len(odd_list) % 2 != 0 and len(even_list) == 0:
        print(-1)
    elif len(odd_list) % 2 == 0 and len(even_list) == 0:
        for i in range(0, len(odd_list)):
            print(odd_list[i], end=" ")
    elif len(odd_list) % 2 == 0 and len(even_list) != 0:
        for i in range(0, len(odd_list)):
            print(odd_list[i], end=" ")
        for i in range(0, len(even_list)):
            print(even_list[i], end=" ")
    else:
        for i in range(0, len(odd_list) - 1):
            print(odd_list[i], end=" ")
        for i in range(0, len(even_list)):
            print(even_list[i], end=" ")

        print(odd_list[len(odd_list) - 1])

    print("\n")