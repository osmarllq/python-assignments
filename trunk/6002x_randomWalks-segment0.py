'''
Here we are going to simulate a random walk. Particuarly, we are going to simulate
the movements of a drunk in a field that moves either nort, south, east or west
in each step. We want to know the position of the drunk, and how far he'll end up
after, say, 1000 steps. Our hypothesis is that he's going to end up far away from
where he started.
We are going to take advantage of python classes to model this problem. Three
classes seem useful to model this problem. Location, a class that will provide
us with methods (functions) to know the position of the drunk in a Field.
By the way, the Field class provides functions to keep track of the movements of
drunk. It provides a function to add a drunk to the field.
'''

class Location(object):
    
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5 #Pitagoras theorem to calculate the
    #distance of the Drunk from the starting position to the current position.
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'





class Field(object):
    
    def __init__(self):
        self.drunks = {} #Start an empty dictionary in wich to add different
                         #types of drunk
        
    def addDrunk(self, drunk, loc): #Add drunk and set startin location
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep() #Function defined below
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]










import random


class Drunk(object): #Abstract class
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk): #A subclass of the Drunk class
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))



def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances



def drunkTest(numTrials = 20):
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print ' Mean =', sum(distances)/len(distances)
        print ' Max =', max(distances), 'Min =', min(distances)


# Carry out the test:
drunkTest()

## import pylab

## #set line width
## pylab.rcParams['lines.linewidth'] = 6
## #set font size for titles
## pylab.rcParams['axes.titlesize'] = 20
## #set font size for labels on axes
## pylab.rcParams['axes.labelsize'] = 20
## #set size of numbers on x-axis
## pylab.rcParams['xtick.major.size'] = 5
## #set size of numbers on y-axis
## pylab.rcParams['ytick.major.size'] = 5
## #set size of markers
## pylab.rcParams['lines.markersize'] = 10
