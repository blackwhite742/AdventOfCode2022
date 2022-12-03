f = open('input.txt')

total_sum = 0

for line in f.readlines():
    line = line.strip()
    
    firstCompartment = line[0:int(len(line)/2)]
    secondCompartment = line[int(len(line)/2)::]
    
    firstSet = set(firstCompartment)
    secondSet = set(secondCompartment)
    
    common = list(firstSet.intersection(secondSet))[0]
    
    total_sum += ord(common)-38 if common.isupper() else ord(common)-96

print(total_sum)


