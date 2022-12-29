n = int(input())
cases = [input() for i in range(n)]
def base10(roman):
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sub = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    out=0
    while roman:
        if roman[:2] in sub:
            out+=num[sub.index(roman[:2])]
            roman=roman[2:]
        else:
            out+=num[sub.index(roman[0])]
            roman=roman[1:]
    return out
def roman(base10):
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sub = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    out=""
    i=12
    while base10:
        div = base10//num[i]
        base10%=num[i]
        while div:
            out+=sub[i]
            div-=1
        i-=1
    return out

for i in cases:
    x=i.split("+")
    x[1]=x[1][:-1]
    #print(base10(x[0])+base10(x[1]))
    if base10(x[0])+base10(x[1])>1000:
        print(i+"CONCORDIA CUM VERITATE")
    else:
        print(i+roman(base10(x[0])+base10(x[1])))