# num=[2,7,11,15]
# target = 9
num=[3,2,4]
target=6
x=[]
for i in range(len(num)):
    for j in range(len(num)-i-1):
        if (num[i]+num[j+i+1])==target:
            x.append(i)
            x.append(j+i+1)
print(x)
        
