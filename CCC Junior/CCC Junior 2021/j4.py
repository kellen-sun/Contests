from collections import Counter
books = list(input())

occurences = dict(Counter(books))
if "L" in occurences.keys():
    l=occurences["L"]
else:
    l=0
if "M" in occurences.keys():
    m=occurences["M"]
else:
    m=0
if "S" in occurences.keys():
    s=occurences["S"]
else:
    s=0
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
