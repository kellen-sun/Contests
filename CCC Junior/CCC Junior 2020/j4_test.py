import sys
input = sys.stdin.readline
t = input()[:-1]
s = input()[:-1]
cyclic = {}
for i in range(len(s)):
    cyclic[s[i:]+s[:i]] = True

for i in range(len(t)-len(s)+1):
    if cyclic.get(t[i:len(s)+i]):
        print("yes")
        sys.exit()
print("no")