s1=input()
s2=input()
a=s2[1]
c=0
for i in s1:
    if a==i:
        c+=1
print("last char of str2 is", a ,"and it appeared ", c ,"times in str1")
