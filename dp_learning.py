
# optimal substructure
# overlapping subproblem

    # memorization(top-down)
    # tabulation (bottom-up)

fib = [-1]*10000

def computeFib(n):
    if n == 0 or n == 1:
        return n
    if fib[n] != -1:
        return fib[n]

    res = computeFib(n-1) + computeFib(n-2)

    fib[n] = res

    return res

print(computeFib(500))




