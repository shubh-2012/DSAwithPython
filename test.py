for _ in range(int(input())):
    x,y = [int(x) for x in input().split()]

    if x*3 == y:
        ans= [y/3,0,0]
        print(ans)
    elif x*3 < y:
        print("NO")
    else:
        a = y//3 + 1
        b = x - a
        c = 3*a - y
        if (b < c):
            print("No")
        elif b > c:
            d = b - c
        else:
            d = b
        e = b-d
        ans = [a,d,e]
        print("YES")
        print(ans)
