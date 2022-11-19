h=int(input(''))
M=int(input(''))
for x in range(1,M+1):
    if -6*x**4+h*x**3+2*x**2+x <=0:
        print('The ballon first touches the ground at hour: ')
        print(x)
        break
    if x == M:
        print('The ballon does not touch ground in the given time. ')
