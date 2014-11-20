### Hash tables

'''
A Hash Table is a technique that implements a very efficient search method.

The basic idea behind a hash table is simple: We convert the key to an integer
and then use that integer to index into a list, which we know can be done in
near constant time.

For instance, a dictionary is a collection of key-value pairs. Hash tables stores
those key-value pairs into a list and provides an efficient way to look for that
key and, hence, to find out what's the value associated with that key.

In principle, values of any object can be easily converted to an integer.
After all, we know that the internal representation of each objet is just a
bunch of bits. And any sequence of bits can bi viewed as representing an integer.
'''

### Function to convert integers to strings.
def strToInt(s):
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)
    return index

#print 'Index =', strToInt('a')
#print 'Index =', strToInt('John is a cool dude')


### Hash Function

'''
A Hash function returns an integer index inside the range of the table.
The modulus offers a way to build a hash function that returns an integer
within a given range.
'''

def hashStr(s, tableSize = 101):
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)%tableSize
    return index

##print hashStr('a')
##print hashStr('John is a cool dude')


print hashStr('Eric', 7)
print hashStr('Chris', 7)
print hashStr('Sarina', 7)


print hashStr('Jill', 7)

'''
'Chris' and 'Jill' got the same index. When two or more keys return the same
index, we have a collision, because both keys are assigned to the same position
in the list or, equivalently, to the same bucket in the hash table. 
'''
