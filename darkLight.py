# cook your dish here
for _ in range(int(input())):
    changes, position = [int(x) for x in input().split()]

    if position == 1:
        if changes % 4 == 0:
            print("On")
        else:
            print("Ambiguous")

    if position == 0:

        if changes % 4 == 0:
            print("Off")
        else:
            print("On")



