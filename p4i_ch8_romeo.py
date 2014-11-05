
file = raw_input('Enter a file name:')

try:
 fhand = open(file)
except:
 print 'File not found'
 exit()

words = []

for i in fhand:
  line = i.split()
  
  for word in line:
     if word in words:
      continue
     else:
      words.append(word)

words.sort()

print words
