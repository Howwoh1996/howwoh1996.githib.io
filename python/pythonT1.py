n1=[1,3,3,4,5,6,7,7,8,13]
x=[]
for i in range(len(n1)):
    for j in range(len(n1)-i-1):
        if n1[i]==n1[j+i+1]:
            x.append(n1[i])
print(x)
        
