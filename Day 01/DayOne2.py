# Advent Of Code --- Day One --- second puzzle

#with open('DayOne1.txt') as file_object:
with open('IndexTest.txt') as file_object:
  inputData = file_object.readlines()

theData = []
for data in inputData:
  theData.append(int(data))

for i in range(len(theData) - 2):
  sum = theData[0] + theData[1] + theData[i+2]
#  print('theData[0] + theData[1] + theData[i+2] = ' + str(theData[0]) + ' + ' + str(theData[1]) + ' + ' + str(theData[i+2]) + ' = ' + str(sum))

def sumPairs():
  for i in range(len(theData) - 1):
    sum = theData[0] + theData[i+1]
    if sum == 2020:
      print('=========== The answer is:  ==============' + str(theData[0] * theData[i+1]))
      break
    if i == len(theData) - 2:
      print('Nothing using ' + str(theData[0]) + ' so eliminating that value from theData.')
      del theData[0]
      print('Length of theData is now ' + str(len(theData)))

#for x in range (len(theData) - 1):
#  sumPairs()

def showIndex():
    for i in range(len(theData)):
        for j in range(i+1, len(theData)):
            print(str(i) + '  ' + str(j))

showIndex()