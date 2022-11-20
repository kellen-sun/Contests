
previous = ""
while True:
    n=input()
    dir = int(sum(list(map(int, list(n[:2])))))
    dis = int(n[2:])
    if n=="99999":
        break
    if dir==0:
        dir=previous
    elif dir%2 == 0:
        dir="right"
        previous = dir
    else:
        dir="left"
        previous = dir
    print(dir, dis)