beats = {
  "A":"Z",
  "B":"X",
  "C":"Y"
}

handValues = {
  "X":1,
  "Y":2,
  "Z":3
}

handTranslations = {
  "A":"X",
  "B":"Y",
  "C":"Z"
}

f = open('day2input.txt')

score = 0

for line in f.readlines():
  opponent,player = line.strip().split(' ')
  if(handTranslations[opponent]==player):
    score+=handValues[player]+3
  elif(beats[opponent]!=player):
    score+=handValues[player]+6
  else:
    score+=handValues[player]

print(score)