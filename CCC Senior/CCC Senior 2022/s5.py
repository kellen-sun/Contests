
def checks(a):
    c=[a[0]+a[1]+a[2], a[3]+a[4], a[5]+a[6]+a[7], a[0]+a[3]+a[5], a[1]+a[6], a[2]+a[4]+a[7], a[0]+a[7],a[5]+a[2]]
    t=True
    for i in c:
        if i%5!=0:
            t=False
            break
    return t
cc=0
for w1 in range(1,10):
    for w2 in range(1,10):
        for w3 in range(1,10):
            for w4 in range(1,10):
                for w5 in range(1,10):
                    for w6 in range(1,10):
                        for w7 in range(1,10):
                            for w8 in range(1,10):
                                if checks([w1,w2,w3,w4,w5,w6,w7,w8]):
                                    cc+=1

print(cc)
