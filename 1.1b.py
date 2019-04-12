sum=0
for i in range(1,31):
    if i%2==0:
        sum-=1/(i*i)
    else:
        sum+=1/(i*i)

print(sum)
