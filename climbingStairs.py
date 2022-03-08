
def climbStairs(n):
    a = [1, 2]
    for i in range(2, 46):
        a.append(a[i - 1] + a[i - 2])

    return a[n-1]


print(climbStairs(5))