
def quickSort(a,l,r):
    if r - l <= 1:
        return

    yellow = l + 1   #for elements less than pivot(generally first element)

    for green in range(l+1 , r):
        if a[green] <= a[l]:
            (a[yellow],a[green]) = (a[green],a[yellow])
            yellow = yellow + 1

        (a[l],a[yellow - 1]) = (a[yellow - 1],a[l])
        quickSort(a,l,yellow-1)
        quickSort(a,yellow,r)


A = [2,3,4,5,7,8,4]
quickSort(A,0,len(A))

print(A)
