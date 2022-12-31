n=int(input())
matrices = []
for i in range(n):
    r,c = map(int, input().split())
    newm = [list(map(int, input().split())) for i in range(r)]
    matrices.append(newm)

def tensor(matrix1, matrix2):
    #tensor product of two matrices
    outmatrix = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            toadd = []
            for a in range(len(matrix1[i])):
                for b in range(len(matrix2[j])):
                    toadd.append(matrix1[i][a]*matrix2[j][b])
            outmatrix.append(toadd)
    return outmatrix
#making the tensor product of all the matrices
final = matrices[0]
for i in range(1,n):
    final = tensor(final, matrices[i])

#doing the outputs
curmax = -float('inf')
curmin = float('inf')
rowsums = []
colsums = []
for i in final:
    rowsums.append(sum(i))
    for j in i:
        if j>curmax:
            curmax = j
        if j<curmin:
            curmin = j
for i in zip(*final):
    colsums.append(sum(i))
print(curmax)
print(curmin)
print(max(rowsums))
print(min(rowsums))
print(max(colsums))
print(min(colsums))