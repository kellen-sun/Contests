k=int(input().split()[-1])
people= sorted(list(map(int, input().split())))
apartments=sorted(list(map(int, input().split())))

people_count=0
apartments_count=0
count=0
while True:
    ap_value=apartments[apartments_count]
    pe_value=people[people_count]
    if ap_value-k>pe_value:
        people_count+=1
    elif ap_value+k<pe_value:
        apartments_count+=1
    else:
        apartments_count+=1
        people_count+=1
        count+=1
    if apartments_count==len(apartments) or people_count==len(people):
        print(count)
        break

