sum=0
silnia=1
x=0.3
for i in range(1,31):
    sum+=(x**i)/(i*silnia)
    silnia*=i

print(sum)
