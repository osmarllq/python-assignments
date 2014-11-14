'''
This script is the same as '6002x_randomwaks0.py' with some additions:
1) We add different types of drunk.
2) We plot, instead of printing, the simulation results.

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
        self.drunks = {} #Start an empty dictionary in which to add several 
                         #drunks, including different types of drunk
        
    def addDrunk(self, drunk, loc):
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
    
class UsualDrunk(Drunk):
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


### Additions:

# Functions to plot the results of drunkTestP()

def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()




    
def drunkTestP1(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    squareRootOfSteps = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken, meanDistances, 'b-',
               label = 'Mean distance')
    pylab.plot(stepsTaken, squareRootOfSteps, 'g-.',
               label = 'Square root of steps')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend()
    pylab.show()



#Look at different kinds of drunks, defined as Drunk sublcasses

#Usual Drunk moves one step either north, south, east or west.
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

#ColdDruk moves less than a whole step when it moves north.
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.95), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

#EDrunk or Euclidian Drunk can move on a diagonal. Indeed, it can move in any direction.
class EDrunk(Drunk):
    def takeStep(self):
        deltaX = random.random()
        if random.random() < 0.5:
            deltaX = -deltaX
        deltaY = random.random()
        if random.random() < 0.5:
            deltaY = -deltaY
        return (deltaX, deltaY)


# New version of simWalks. It allows different types of Drunk

def simWalks(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

# Added a loop to drunkTestP() to iterate over classes of drunk.
def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    for dClass in (UsualDrunk, ColdDrunk, EDrunk):
        meanDistances = []
        for numSteps in stepsTaken:
            distances = simWalks(numSteps, numTrials, dClass)
            meanDistances.append(sum(distances)/len(distances))
        pylab.plot(stepsTaken, meanDistances,
                   label = dClass.__name__)
        pylab.title('Mean Distance from Origin')
        pylab.xlabel('Steps Taken')
        pylab.ylabel('Steps from Origin')
        pylab.legend(loc = 'upper left')
    pylab.show()

'''
Abstract data types make life easier. Because we had Location, Drunks and Fields
we could, in a very straightforward way, write the simulation itself. Alos, we
saw that subclassing is useful. Because we started with the abstract class Drunk,
we could then create several sublcasses that would let us explore the behavior of
different kinds of drunk. Once the basic structure is in place, we can try different
experiments. We can play with different length walks, with different kind of drunks, etc.
Finally, we saw that we can use plotting to get insight into trends: how things
change with respect to the number of steps.
'''

