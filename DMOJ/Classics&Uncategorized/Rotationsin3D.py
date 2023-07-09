import math
t = int(input())
out = []

def dot(x,y):
    c=0
    for i in range(3):
        c+=x[i]*y[i]
    return c

def matrixmultiply(M, V):
    return [dot(M[0], V), dot(M[1], V), dot(M[2], V)]

def rotate(x,y,z,rx,ry,rz,theta):
    magnitude = (rx**2+ry**2+rz**2)**0.5
    ux, uy, uz = rx/magnitude, ry/magnitude, rz/magnitude
    c = math.cos(theta)
    s = math.sin(theta)
    R = [
        [c + ux**2 * (1-c), ux*uy*(1-c)-uz*s, ux*uz*(1-c)+uy*s],
        [uy*ux*(1-c)+uz*s, c+uy**2 *(1-c), uy*uz*(1-c)-ux*s],
        [uz*ux*(1-c) - uy*s, uz*uy*(1-c)+ux*s, c+uz**2 *(1-c)]
    ]
    return matrixmultiply(R, (x,y,z))


for i in range(t):
    x,y,z,rx,ry,rz,theta = map(float, input().split())
    out.append(rotate(x,y,z,rx,ry,rz,theta))

for i in out:
    print("{:.6f}".format(i[0]), "{:.6f}".format(i[1]), "{:.6f}".format(i[2]))