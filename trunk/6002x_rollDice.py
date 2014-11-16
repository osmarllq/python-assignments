import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

print rollN(5)

def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        result = rollN(numRolls)
        if result == goal:
            return numTries

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    print 'Average number of tries =', total/float(numTrials)

##runSim('11111', 100)
##runSim('54324', 100)
''' NOTE:
If you have a string of n digits, with X different digits, then you have x^n
possible combinations of those digits. For a die, which has six different digits,
then there are 6^n posible combinations of those six digits. So, for instance,
for a six sided die there are 6^5 possible seuences of length five. Then, the
probability of getting five ones is 1/(6^5) or one out of every 7776 cases,
wich is the same probability of getting any other sequence of five numbers
(like 54324). This simulation throws out that the probability of getting the
sequence '11111' or '54324' is about the same and close to 1/(6^5) or 0.00001286
'''

def atLeastOneOne(numRolls, numTrials):
    numSuccess = 0
    for i in range(numTrials):
        rolls = rollN(numRolls)
        if '1' in rolls:
            numSuccess += 1
        fracSuccess = numSuccess/float(numTrials)
    print fracSuccess

atLeastOneOne(10, 1000)

''' NOTE:
The probability of not getting a one in n rolls of a die is (5/6)^n. Hence,
for instance, in ten (10) rolls of a die the probability of not getting a one
is (5/6)^10. Then, what's the probability of getting a one? We already know the
probability of NOT getting a one: (5/6)^n. Then, the probability of getting at
least one one is 1 - (5/6)^n. For ten rolls this is 1 - (5/6)^10 = 0.83849.
The simulation confirms such a guess, as the estimated probability is close to
the theoretical one.
'''

