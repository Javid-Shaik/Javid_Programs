n = int(input("Enter a number : "))
temp = n
reverse_num = 0
while n>0:
    reverse_num = reverse_num*10+(n%10)
    n = n//10

print(temp,"is palindrome") if temp==reverse_num else print(temp,"is not palindrome")
