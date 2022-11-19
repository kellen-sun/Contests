from collections import Counter
books = list(input())

occurences = dict(Counter(books))
l=occurences["L"]
m=occurences["M"]
s=occurences["S"]
c=0
l_in_m=0
m_in_l=0
misplaced_m=0
misplaced_l=0
for i in range(l):
    if books[i] == "M":
        m_in_l += 1
        misplaced_l += 1
    elif books[i] == "S":
        misplaced_l += 1

for i in range(l, l + m):
    if books[i] == "L":
        l_in_m += 1
        misplaced_m += 1
    elif books[i] == "S":
        misplaced_m += 1

print(misplaced_l + misplaced_m - min(m_in_l, l_in_m))
