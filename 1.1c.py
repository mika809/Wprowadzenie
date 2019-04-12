sum=0
silnia=1
for i in range(1,31):
    if i%2!=0:
        sum-=1/(i*silnia)
    else:
        sum+=1/(i*silnia)
    silnia*=i
print(sum)
