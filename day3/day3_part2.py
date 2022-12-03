f = open('input.txt')

total_sum = 0

items = set()

for ctr,line in enumerate(f.readlines(),1):
    line = line.strip()
    
    if(len(items)==0):
        items = set(line)
    else:
        items = items.intersection(set(line))

    if (ctr%3 == 0):
        common = list(items)[0] if len(items)>0 else '/'
        total_sum += ord(common)-38 if common.isupper() else ord(common)-96
        items = set()


print(total_sum)


