# Advent Of Code --- Day Two --- first puzzle

countGoodPassword = 0
lineCount = 0

#with open('DayTwo.txt') as file_object:
with open('DayTwoSimple.txt') as file_object:
  inputData = file_object.readlines()
for line in inputData:
  lineCount += 1
  charCount = 0
  firstSplit = line.split(":")
  #print('firstSplit[0] = ' + firstSplit[0] + '  and   firstSplit[1] = ' + firstSplit[1])
  secondSplit = firstSplit[0].split("-")
  #print('secondSplit[0] = ' + secondSplit[0] + '  and   secondSplit[1] = ' + secondSplit[1])
  thirdSplit = secondSplit[1].split()
  #print('Looking for ' + thirdSplit[1] + ' min = ' + secondSplit[0] + ' and max = ' + thirdSplit[0] + ' in ' + firstSplit[1].rstrip())
  password = firstSplit[1].rstrip()

  if password.count(thirdSplit[1]) >= int(secondSplit[0]):
    if password.count(thirdSplit[1]) <= int(thirdSplit[0]):
        countGoodPassword += 1
        print('Line ' + str(lineCount) + '   password = ' + password + ' is Good, and countGoodPassword = ' + str(countGoodPassword))