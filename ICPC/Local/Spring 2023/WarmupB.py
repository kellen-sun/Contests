out = []
while True:
    s = input()
    if s=="-":
        break
    seen = [0 for i in range(26)]
    for i in s:
        if i!=" ":
            seen[ord(i)-65] = seen[ord(i)-65] | 1
    if all(seen):
        out.append("Sufficient.")
    else:
        out.append("Deficient.")
for i in out:
    print(i)
