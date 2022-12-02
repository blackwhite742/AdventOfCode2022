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

beaten = dict(zip(beats.values(),beats.keys()))

f = open('input.txt')

score = 0

for line in f.readlines():

  opponent,player = line.strip().split(' ')

  if(player == 'X'):
    # Lose
    score+=handValues[beats[opponent]]
  
  elif(player == 'Y'):
    # Draw
    score+=handValues[handTranslations[opponent]]+3
  
  elif(player == 'Z'):
    # Win
    score+=handValues[handTranslations[beaten[handTranslations[opponent]]]]+6
  

print(score)