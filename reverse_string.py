def rev_str(str):
    n = len(str)
    for i in range(n-1,-1,-1):
        print(str[i],end="")

rev_str("qwerty")