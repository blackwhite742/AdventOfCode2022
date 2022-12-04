f = open("input.txt")

def isFullyContained(firstInterval,secondInterval):
    return (secondInterval[0]>=firstInterval[0] and secondInterval[1]<=firstInterval[1])

ctr = 0

for line in f.readlines():
    line = line.strip()

    firstInterval,secondInterval = line.split(',')

    first = tuple([int(el) for el in firstInterval.split('-')])
    second = tuple([int(el) for el in secondInterval.split('-')])

    ctr += (isFullyContained(first,second) or isFullyContained(second,first))

print(ctr)