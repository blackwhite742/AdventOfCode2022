f = open("input.txt")

def overlaps(firstInterval,secondInterval):
    return (firstInterval[0]>=secondInterval[0] and firstInterval[0]<=secondInterval[1]) or (firstInterval[1]>=secondInterval[0] and firstInterval[1]<=secondInterval[1])

ctr = 0

for line in f.readlines():
    line = line.strip()

    firstInterval,secondInterval = line.split(',')

    first = tuple([int(el) for el in firstInterval.split('-')])
    second = tuple([int(el) for el in secondInterval.split('-')])

    ctr += (overlaps(first,second) or overlaps(second,first))

print(ctr)