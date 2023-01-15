n=int(input())
def figure_out(n):
    start=1
    dig=1
    while start<n:
        start+=9*10**(dig-1)
        dig+=1
    dig=dig-1
    other=start-(start-9*10**(dig))
    number=(other)//dig
    print(number)


print(figure_out(n))
