s="ducat mohannagar"
x=-1
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='u' or i=='o'):
        x=s.index(i,x+1)
        print("vowels",i,x)
    else:
        x=s.index(i,x+1)
        print("It is consonant",i,x)
