for _ in range(int(input())):
    n, target = [int(x) for x in input().split()]
    correct_ans = 0
    wrong_ans = 0
    unattempted = 0
    x = 0
    if target//3 > n:
        x = 1
    
    elif target%3 == 0:
        correct_ans = target//3
        unattempted = n - correct_ans
    else:
        if target//3 == n:
            correct_ans = n
        else:
            correct_ans = target//3 + 1
            wrong_ans = correct_ans*3 - target
            if wrong_ans > (n - correct_ans):
                x = 1
            else:
                unattempted = n - (wrong_ans+correct_ans)

    if x == 1:
        print("NO")
    else:
        print("Yes")
        print(correct_ans,wrong_ans,unattempted)
