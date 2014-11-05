file = raw_input('Enter a file name:')

try:
 fhand = open(file)
except:
 print 'File not found'
 exit()

count = 0

for j in fhand:
  words = j.split()   
  
  if len(words) > 0 and words[0] == 'From':
    sender = words[1]
    count = count + 1
    print sender
    
print 'There were %d lines with %s as the first word' % (count, 'From')
    
   