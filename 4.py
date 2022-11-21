R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
M = []
print("Enter the entries rowwise:")
for i in range(R):  
    a =[]
    for j in range(C): 
         a.append(int(input()))
    M.append(a)
s=[]
for i in range(R):
    for j in range(C):
        if M[i][j]==0:
            s.append([i,j])
temp=s[0][1]
for i in range(len(s)):
    if temp<s[i][1]:
        temp=s[i][1]
temp1=s[0][0]
for i in range(len(s)):
    if temp1<s[i][0]:
        temp1=s[i][0]
temp2=s[0][0]
temp3=s[0][1]
print((temp2,temp3),(temp2,temp),(temp1,temp3),(temp1,temp))
