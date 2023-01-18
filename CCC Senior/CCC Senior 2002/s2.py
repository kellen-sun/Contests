n = int(input())
m = int(input())
from fractions import Fraction
l = Fraction(n, m)
num = l.numerator
den = l.denominator

whole = num//den
left = num%den
if left == 0:
    print(whole)
elif whole!=0:
    print(whole, str(left)+"/"+str(den))
else:
    print(str(left)+"/"+str(den))
