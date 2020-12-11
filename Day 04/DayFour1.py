# Advent Of Code --- Day Four --- first puzzle

countValidPassports = 0
countInvalidPassports = 0
countAllPassports = 0

with open('DayFour.txt') as file_object:
#with open('Simple Input Data.txt') as file_object:
#with open('TwentyOnePassports.txt') as file_object:
  inputData = file_object.readlines()
for line in inputData:
  if line == '\n':
    countAllPassports +=1
print('Number of passports = ' + str(countAllPassports + 1))

singleLineData = []
tempLine = ''
for line in inputData:
  if line != '\n':
    tempLine = tempLine + line.replace('\n', ' ')
  else:
    singleLineData.append(tempLine)
    tempLine = ''
singleLineData.append(tempLine)  # Last line of file not followed by \n

lineNumber = 1
for passport in singleLineData:
    dataFields = passport.split()
    dataFields.sort()
    if len(dataFields) == 8:
        countValidPassports +=1
        print('Passport number ' + str(lineNumber) + ' is valid with 8 fields.')
    elif len(dataFields) == 7:
        valid = True
        for field in dataFields:
 #           print(field)
            nameValue = field.split(':')
 #          print(nameValue[0])
            if nameValue[0] == 'cid':
                valid = False
        if valid == True:
            countValidPassports +=1
            print('Passport number ' + str(lineNumber) + ' is valid with 7 fields.')
    else:
        countInvalidPassports +=1
        print('Passport number ' + str(lineNumber) + ' is NOT valid.')
    lineNumber +=1
      
print('Number of valid passports = ' + str(countValidPassports))
print('Number of invalid passports = ' + str(countInvalidPassports))