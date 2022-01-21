s="ducat mohannagar 134 "
print(len(s))
vowel=0
consonant=0
space=0
digit=0
for i in s:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel=vowel+1
    if (i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9'):
        digit=digit+1
    elif(i==' '):
        space=space+1
    else:
        consonant=consonant+1
print("Total vowel alphabets are ",vowel)
print("Total consonants alphabets are ",consonant)
print("Total white space are ",space)
print("Total number of digit are ",digit)


    
