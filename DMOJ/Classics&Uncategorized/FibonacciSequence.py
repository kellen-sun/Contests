n = int(input())
MOD = 1000000007
#maybe closed forms in terms of raising int to powers by using binomial theorem?

def dot(v,w):
    global MOD
    return (v[0]*w[0]+v[1]*w[1])%MOD

def matrixmult(A,B):
    return [
        [dot(A[0], [B[0][0], B[1][0]]), dot(A[0], [B[0][1], B[1][1]])],
        [dot(A[1], [B[0][0], B[1][0]]), dot(A[1], [B[0][1], B[1][1]])]
    ]

def matrixpow(M, n):
    if n == 1:
        return M
    if n==2:
        return matrixmult(M, M)
    else:
        if n%2==0:
            return matrixpow(matrixpow(M, n//2), 2)
        else:
            return matrixmult(matrixpow(M, n//2), matrixpow(M, n//2+1))

print(matrixpow([[1,1],[1,0]], n%2000000016)[0][1])