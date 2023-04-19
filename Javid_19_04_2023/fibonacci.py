n = int(input("Enter a number : "))   
a , b = 0 , 1
if n<1:
    print("Enter a valid limit")
else:
    print(a,b,end=" ")
    c = a+b
    while c<n:
        print(c,end=" ")
        a = b
        b = c
        c = a+b
