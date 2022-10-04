for _ in range(int(input())):
    police, thief = [int(x) for x in input().split()]

    if police == thief:
        print(0)
    elif police < thief:
        print(thief-police)
    else:
        print(police-thief)

