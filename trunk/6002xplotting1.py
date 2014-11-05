import os
os.getcwd()
os.chdir("c:/users/osmar/downloads")

def loadData(x):
  inFile = open(x)
  high = []
  low = []
  for line in inFile:  
    fields = line.split()
    high.append(int(fields[1]))
    low.append(int(fields[2]))
  return (low,high)

data = loadData('julyTemps.txt')

def producePlot(lowTemps, highTemps):
 diffTemps = []
 for i in range(len(lowTemps)):
  diff = highTemps[i]-lowTemps[i]
  diffTemps.append(diff)
 pylab.figure('Temps')
 pylab.plot(range(1,32),diffTemps)
 pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
 pylab.xlabel('Days')
 pylab.ylabel('Temperature Ranges')
 pylab.show()


producePlot(data[0],data[1])