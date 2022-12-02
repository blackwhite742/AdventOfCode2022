f = open("day1input.txt")

sums = []
tempSum = 0
for line in f.readlines():
  if(line=='\n'):
    sums.append(tempSum)
    tempSum = 0
  else:
    tempSum+=int(line)

sums.sort()

print(sum(sums[-3:]))