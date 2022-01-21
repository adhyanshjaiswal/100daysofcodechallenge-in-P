num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

max=max(num1,num2)
while(True):
    if(max%num1 == 0 and max % num2 ==0):
        print("LCM of two number is",max)
        break
    max=max+1
