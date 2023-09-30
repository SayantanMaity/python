# wapp to find sum of digits of the numbers appering withing a given range of natural number
L=int(input("enter the lower limit:"))
U=int(input("enter the upper limit:"))
for n in range(L,U+1):
    sum = 0
    bkup = n
    if n<0:
        n=-n
    while n>0:
        r=n%10
        sum=sum+r
        n= n//10
    print("sum of all digits of",bkup,"is=",sum)
