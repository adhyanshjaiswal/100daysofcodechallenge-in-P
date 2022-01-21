s=input("Enter the string:")
char=input("Enter the character which you want to count:")
count=0

for i in range(len(s)):
    if (s[i]==char):
        count=count+1
        print("The frequency of characters in a string is",count)
