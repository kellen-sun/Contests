a=int(input())
for x in range(a):
    for y in range(x):
        print('*', end="", flush=True)
    for c in range(2*a-2*x):
        print(' ',  end="", flush=True)
    for y in range(x):
        print('*', end="", flush=True)
    print('')
        
for x in range(a):
    for y in range(a-x):
        print('*', end="", flush=True)
    for c in range(2*x):
        print(' ',  end="", flush=True)
    for y in range(a-x):
        print('*', end="", flush=True)
    print('')
