t=int(input())
for _ in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    list1=sorted(list1)
    res=0
    c=0
    temp=2 
    i=0
    while i<n:
        if list1[i]>=temp:
            temp*=2 
            if c>1:
                c-=1
                res+=((c*(c+1))//2)
            c=0
        else:
            c+=1 
            i+=1
    if c>1:
        c-=1
        res+=((c*(c+1))//2)
    print(res)    
        
