import sys
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
'''
d2=(s1[0]-s2[0])**2+(s1[1]-s2[1])**2
x = (d2-s1[2]+s2[2]/(2* d2**0.5))
if s1[2]>s2[2] and x<d2**0.5-x:
    x=d2**0.5-x
if s1[2]+s2[2]<d2**0.5:
    print("AaAAA")
    sys.exit()
h2=s2[2]-x**2
midpoint = (s2[0]+(s1[0]-s2[0])*x/d2**0.5, s2[1]+(s1[1]-s2[1])*x/d2**0.5)
#print(midpoint, h2)
if s1[1]!=s2[1]:
    slope = (s1[0]-s2[0])/(s1[1]-s2[1])
    final = (h2**0.5 / (slope**2 + 1.0)**0.5, h2**0.5 / ((slope**2 + 1.0)**0.5) * slope)
else:
    final = (midpoint[0], midpoint[1]+h2**0.5)
final2 = (2*midpoint[0]-final[0], 2*midpoint[1]-final[1])

#print(final, final2)
if (final[0]-s3[0])**2+(final[1]-s3[1])**2==s3[2]:
    final = (round(final[0]), round(final[1]))
    print(*final)
elif (final2[0]-s3[0])**2+(final2[1]-s3[1])**2==s3[2]:
    final2 = (round(final2[0]), round(final2[1]))
    print(*final2)
else:
    print(s1,s2,s3)'''

for i in range(1000000):
    for j in range(1000000):
        if (i-s1[0])**2+(j-s1[1])**2==s1[2] and (i-s2[0])**2+(j-s2[1])**2==s2[2] and (i-s3[0])**2+(j-s3[1])**2==s3[2]:
            print(i,j)
            sys.exit()