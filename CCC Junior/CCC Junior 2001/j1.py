n=int(input())
for i in range(n//2+1):
    print("*"*(2*i+1)+(2*n-2-4*i)*" "+"*"*(2*i+1))
for i in range(n-2, -1, -2):
    print("*"*i+(2*n-2*i)*" "+"*"*i)