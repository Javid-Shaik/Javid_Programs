a ,b,c =map(int,input("Enter a,b,c sperated with space : ").split())

if a>b and a>c :
    if b>c:
        temp = a
        a = c
        c = temp
    else :
        temp = a
        a = b
        b = c
        c = temp
elif b>c and b>a :
    if a>c:
        temp = b
        b = a
        a = c
        c = temp
    else :
        temp = b
        b = c
        c = temp
else:
    if a>b:
        temp = a
        a = b
        b = temp
print(a,b,c)
    
