num=int(input())
l=num%10
temp=num//10
c=0
while num:
    r=num%10
    num=num//10
    c=c+1
temp=temp*10+r
temp=temp%pow(10,c-1)
if l==0:
    l=0
temp=l*pow(10,c-1)+temp
print(temp)