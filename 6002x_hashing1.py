### Hash Tables

'''
Hash tables are the way dictionaries are implemented in Python.

Here we will create a dictionary and provide a way to manage collisions.
A simple way to deal with collisions consists in assigning the colliding keys
to the same bucket.
Then a dictionary can be represented as a list of buckets, where each bucket is
a list of key-value tuples. By making each bucket a list, we handle collisions
by storing all the values that hash to that bucket.

There are many other ways to handle collisions, some considerably better than
using lists. However, this is probably the simplest mechanism. It works fine if
the hash table is big enough and the hash function provides a good enough
approximation to a uniform distribution. Namely, the collisions should be
uniformly distributed.

In this example our keys are going to be numbers, not strings.
'''

import random


class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    '''
    addEntry takes the key and the value. It starts by finding the correct bucket.
    It does that by taking the key and then hashing using modulus. It's then going
    to go look at the hash bucket until it finds the dictionary key. If it does,
    it updates it and then returns. Notice that once it's returned, it's done.
    On the other hand, if it finishes the loop with without finding the key, then
    it just adds a new tuple (dictKey, dictVal) to the dictionary.

    Finaly, notice the use of aliasing here. The found bucket is assigned to
    "hashBucket", namely, "hashBucket = self.buckets[...]". Then hashBucket and
    "self.buckets[dictKey%self.numBuckets]" are aliases of the same object.
    As a consequence, any modifications done to "hashBucket" are inmediatly iherited
    by "self.buckets[...]". So, when a new tuple is added to the object "hashBucket"
    this is also added to "self.buckets[...]".
    '''
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return # If the loop returns, it finishes here and never
                       # executes the last line of the function.
        hashBucket.append((dictKey, dictVal)) # If a key is not found the loop
                       # will not return any value and this line will be executed.
        
    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
        
    def __str__(self):
        res = ''   # Change 1
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return '{' + res[:-1] + '}' # #res[:-1] removes the last comma
    
D = intDict(29)
for i in range(20):
    #choose a random int in range(10**5)
    key = random.choice(range(10**5))
    D.addEntry(key, i)

print '\n', 'The buckets are:'
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket














