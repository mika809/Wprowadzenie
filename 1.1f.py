sum=0
silnia=1
x=0.3
for i in range(1,31,4):
    for k in range(1,(i+1)):
        silnia*=k
    sum+=(x**i)/(i*silnia)
    silnia=1
silnia=1
for l in range(3,31,4):
        for m in range(1,(l+1)):
            silnia*=m           
        sum-=(x**l)/(l*silnia)
        silnia=1
print(sum)
