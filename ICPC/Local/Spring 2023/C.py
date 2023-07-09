s = input()

c = 0

prev = s[0]
for i in range(1, len(s)):
    if s[i]==prev:
        c+=1
    prev = s[i]
print((c+1)//2)
