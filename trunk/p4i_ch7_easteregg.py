file = raw_input('Enter a file name:')

try:
 fhand = open(file)
except:
 if file == 'na na boo boo':
  print "NA NA BOO BOO TO YOU - You have been punk'd!"
 else:
  print 'File cannot be opened:', file
 exit()

total = 0
count = 0

for line in fhand:
  if line.find('X-DSPAM-Confidence:') == -1 : 
      continue

  pos = line.find(':')
  value = line[pos+1:]
  value = float(value)
  total = total + value
  count = count + 1

print 'Average spam confidence:', total/count   