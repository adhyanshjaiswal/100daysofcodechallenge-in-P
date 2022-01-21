s="ducat mohan"
x=s.split()
#t=x[0]
y=x[1]
x=x[0][0:1].upper() + x[0][1:len(x[0])-1] +x[0][len(x[0])-1:len(x[0])].upper() + " " + y[0:1].upper()+ y[1:len(y)-1] + y[len(y)-1:len(y)].upper()


print(x)
