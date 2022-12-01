f = open("day1input.txt")

maxSum = 0
tempSum = 0
for line in f.readlines():
  if(line=='\n'):
    maxSum = max(maxSum,tempSum)
    tempSum = 0
  else:
    tempSum+=int(line)

print("Maximum is",maxSum)