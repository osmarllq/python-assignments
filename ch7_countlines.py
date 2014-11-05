import os
os.chdir("C:\Users\USUARIO\Documents\python-prog\myProgAssignments")

fhand = open('mbox.txt')
count = 0
for line in fhand:
 count = count + 1
print 'Line Count:', count