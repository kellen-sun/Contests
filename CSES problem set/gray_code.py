n=int(input())
start = [0 for i in range(n)]
def push(bits):
    count=len(bits)-1
    for x in range(len(bits)):
        if bits[count]==1:
            bits[count]=0
            count=count-1
        else:
            break
    bits[count]=1
    return bits
for x in range(2**n):
    print(*start,sep='')
    start=push(start)
