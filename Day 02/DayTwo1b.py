# Advent Of Code --- Day Two --- first puzzle

countGoodPassword = 0

#with open('DayTwo1.txt') as file_object:
with open('DayTwoSimple.txt') as file_object:
  inputData = file_object.readlines()
for line in inputData:
  charCount = 0
#  print('Data input = ' + line)
  firstSplit = line.split(":")
#  print('firstSplit[0] = ' + firstSplit[0] + '  and   firstSplit[1] = ' + firstSplit[1])
  secondSplit = firstSplit[0].split("-")
#  print('secondSplit[0] = ' + secondSplit[0] + '  and   secondSplit[1] = ' + secondSplit[1])
  thirdSplit = secondSplit[1].split()
  print('Looking for ' + thirdSplit[1] + ' min = ' + secondSplit[0] + ' and max = ' + thirdSplit[0] + ' in ' + firstSplit[1].rstrip())
  password = firstSplit[1].rstrip()
  characters = list(password.strip())
  print(characters)
  for char in characters:
    if thirdSplit[1] in characters:
      characters.remove(thirdSplit[1])
      charCount +=1
    print(charCount)
  if charCount >= int(secondSplit[0]):
    if charCount <= int(thirdSplit[0]):
      countGoodPassword += 1
      print (firstSplit[1] + ' is good, and countGoodPassword = ' + str(countGoodPassword) )
