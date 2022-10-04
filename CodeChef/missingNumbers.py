for _ in range(int(input())):
    A, B, C, D = [int(x) for x in input().split()]

    listElement = [A, B, C, D]
    listElement.sort()
    count = 0
    temp = 0
    if count == 0:
        diff = listElement[0]
        div = listElement[1]
        sumAB = listElement[2]
        mult = listElement[3]

        a = (diff + sumAB) / 2

        b = a - diff

        if b != 0:

            if a // b != div or a * b != mult:
                count = 1
            else:
                temp = 1
        else:
            count = 1
    if count == 1:
        diff = listElement[0]
        div = listElement[1]
        sumAB = listElement[3]
        mult = listElement[2]
        a = (diff + sumAB) / 2

        b = a - diff

        if b != 0:

            if a // b != div or a * b != mult:
                count = 2
            else:
                temp = 1
        else:
            count = 2

    if count == 2:
        diff = listElement[1]
        div = listElement[0]
        sumAB = listElement[2]
        mult = listElement[3]

        a = (diff + sumAB) / 2

        b = a - diff

        if b != 0:

            if a // b != div or a * b != mult:
                count = 3
            else:
                temp = 1
        else:
            count = 3
    if count == 3:
        diff = listElement[1]
        div = listElement[0]
        sumAB = listElement[3]
        mult = listElement[2]
        a = (diff + sumAB) / 2

        b = a - diff

        if b != 0:

            if a // b != div or a * b != mult:
                count = 3
            else:
                temp = 1

    if temp != 1:
        print(-1, -1)

    else:
        if int(a) >= 1 and int(a) <= 10000 and int(b) >= 1 and int(b) <= 10000:
            print(int(a), int(b))

        else:
            print(-1, -1)