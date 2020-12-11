# Advent Of Code --- Day One
with open('DayOne1.txt') as file_object:
  inputData = file_object.readlines()

theData = []
for data in inputData:
  theData.append(int(data))

for i in range(len(theData) - 1):
  sum = theData[0] + theData[i+1]
#  print('theData[0] + theData[i+1] = ' + str(theData[0]) + ' + ' + str(theData[i+1]) + ' = ' + str(sum))

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

for x in range (len(theData) - 1):
  sumPairs()