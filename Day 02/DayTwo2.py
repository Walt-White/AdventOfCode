# Advent Of Code --- Day Two --- second puzzle

countGoodPassword = 0
lineCount = 0

#with open('DayTwo.txt') as file_object:
with open('DayTwoSimple.txt') as file_object:
  inputData = file_object.readlines()
for line in inputData:
  lineCount += 1
  placeCount = 0  # Want to see 1 for success.  0 and 2 fail.
  firstSplit = line.split(":")
  #print('firstSplit[0] = ' + firstSplit[0] + '  and   firstSplit[1] = ' + firstSplit[1])
  secondSplit = firstSplit[0].split("-")
  #print('secondSplit[0] = ' + secondSplit[0] + '  and   secondSplit[1] = ' + secondSplit[1])
  thirdSplit = secondSplit[1].split()
  #print('Looking for ' + thirdSplit[1] + ' min = ' + secondSplit[0] + ' and max = ' + thirdSplit[0] + ' in ' + firstSplit[1].rstrip())
  password = firstSplit[1].rstrip()
  characters = list(password)
  
  print('============== ')
  print(line.strip())
  print('Looking for ' + thirdSplit[1] + ' in position ' +  secondSplit[0] + ' and at position ' + thirdSplit[0])
  if characters[int(secondSplit[0])] == thirdSplit[1]:
    placeCount += 1
  if characters[int(thirdSplit[0])] == thirdSplit[1]:
      placeCount += 1
  if placeCount == 1:
    countGoodPassword += 1
    print('Line ' + str(lineCount) + '   password = ' + password + ' is Good, and countGoodPassword = ' + str(countGoodPassword))

#  if password.count(thirdSplit[1]) >= int(secondSplit[0]):
#    if password.count(thirdSplit[1]) <= int(thirdSplit[0]):
#        countGoodPassword += 1
#        print('Line ' + str(lineCount) + '   password = ' + password + ' is Good, and countGoodPassword = ' + str(countGoodPassword))