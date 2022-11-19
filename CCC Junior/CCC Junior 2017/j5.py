n=input()
boards = input().split()
boardlengths = [0 for i in range(2001)]
fences = [0 for i in range(4001)]
for board in boards:
    boardlengths[int(board)] += 1
for i in range(2000):
    fences[2*i] += boardlengths[i] // 2
    for j in range(i+1, 2001):
        fences[i + j] += min(boardlengths[i], boardlengths[j])
longest, size = max(fences), fences.count(max(fences))
print(str(longest)+' '+str(size))
