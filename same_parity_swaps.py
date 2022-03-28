# cook your dish here
for _ in range(int(input())):
    size = int(input())
    inputList = input()
    odd_parity = []
    even_parity = []
    for i in range(0,size):
        if i % 2 == 0:
            even_parity.append(inputList[i])
        else:
            odd_parity.append(inputList[i])

    even_parity.sort()
    odd_parity.sort()
    poss1 = ""
    poss2 = ""
    poss3 = ""
    j, k = 0, 0
    for i in range(0,size):
        if i % 2 == 0:
            poss1+=(even_parity[j])
            poss2+=(even_parity[j])
            poss3+=(even_parity[len(even_parity)-1-j])
            j += 1
        else:
            poss1+=(odd_parity[k])
            poss2+=(odd_parity[len(odd_parity)-1-k])
            poss3+=(odd_parity[k])
            k += 1

    ans = max(poss1.count("01"), poss2.count("01"),poss3.count("01"))
    # print(even_parity)
    # print(odd_parity)
    # print(poss2)
    # print(poss1)
    print(ans)


