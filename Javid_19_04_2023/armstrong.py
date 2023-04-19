n = int(input("enter a number : "))
temp = n
digits = 0
while n>0:
    n = n//10
    digits+=1

arms = 0
n = temp 
while temp>0:
    arms += (temp%10)**digits
    temp = temp//10

if arms == n:
    print(n,"is armstrong number")
else :
    print(n,"is not an armstrong number")
