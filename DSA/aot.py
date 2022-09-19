#area of triangle

a = float(input('enter first side: '))
b = float(input('enter second side: '))
c = float(input('enter third side: '))

#semiperimeter
s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('area of triangle with sides',a,b,c,'is: ',area)
