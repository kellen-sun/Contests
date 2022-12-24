n = int(input())
cipher = [input().split() for i in range(5)]
out = []
not_included = [chr(i) for i in range(97, 123)]
for i in range(5):
    for j in range(5):
        not_included.remove(cipher[i][j])
not_included=not_included[0]
for i in range(n):
    o=""
    k=input()
    for ii in range(len(k)):
        j=k[ii]
        if j==not_included:
            o+=not_included
        elif 65<=ord(j)<70:
            a=ord(j)-65
            b=int(k[ii+1])-1
            o+=cipher[a][b]
    out.append(o)
for i in out: print(i)
