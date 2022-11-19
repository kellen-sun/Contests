a=int(input(''))
b=int(input(''))
sumac=[a, b]
while True:
    if sumac[-1]>sumac[-2]:
        break
    sumac.append(sumac[-2]-sumac[-1])
print(len(sumac))
