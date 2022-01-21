n=int(input("enter the  number:"))
reversed=0
while(n>0):
    a=n%10
    reversed = reversed*10 +a
    n=n//10
print(reversed)
