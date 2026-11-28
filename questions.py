a = int(input())
if a % 2 == 0:
    print("Even number")
else :
    print("Odd number")


a = int(input())
b = int(input())
c = int(input())
if a > b and a > c :
    print("a is the greatest number")
elif b > a and b > c :
    print("b is the greatest number")
else :
    print("c is the greatest number")


n = int(input())
for i in range(2,n):
    if n % i == 0:
        print("not prime")
        break
    else:
        print("prime")



n = int(input())
a = 0 
b = 1 
for i in range(n):
    print(a)
    c = a + b 
    a = b 
    b = c
    